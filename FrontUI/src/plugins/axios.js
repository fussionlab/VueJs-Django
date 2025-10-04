"use strict";

import Vue from 'vue';

// --- 1. Custom axios Wrapper to Replace axios.create() ---

// Function to perform the actual axios request
const baseaxios = (url, options = {}) => {
  return fetch(url, options)
    .then(response => {
      // axios does not throw on HTTP errors (4xx or 5xx), so we handle it here.
      if (!response.ok) {
        // Create an Error object that includes the response for the interceptor
        const error = new Error(`HTTP error! status: ${response.status}`);
        error.response = response;
        throw error;
      }
      return response;
    });
};

// The custom axios instance that will hold interceptors
const _axios = {
  requestInterceptors: [],
  responseInterceptors: [],
  
  // Method to mimic the axios request structure
  async request(url, options = {}) {
    let finalConfig = { url, ...options };

    // Run Request Interceptors
    for (const interceptor of this.requestInterceptors) {
      try {
        finalConfig = interceptor(finalConfig);
      } catch (error) {
        // If a request interceptor rejects, stop the chain and run error handlers
        return Promise.reject(error);
      }
    }

    // Perform axios
    try {
      let response = await baseaxios(finalConfig.url, finalConfig);
      
      // Run Response Interceptors (Success)
      for (const interceptor of this.responseInterceptors) {
        response = interceptor.fulfilled ? interceptor.fulfilled(response) : response;
      }
      return response;
    } catch (error) {
      // Run Response Interceptors (Error)
      for (const interceptor of this.responseInterceptors) {
        if (interceptor.rejected) {
          error = interceptor.rejected(error);
        }
      }
      return Promise.reject(error);
    }
  },

  // Simplified methods (get, post, etc.) that call the request method
  get(url, options = {}) {
    return this.request(url, { ...options, method: 'GET' });
  },
  post(url, data, options = {}) {
    return this.request(url, { ...options, method: 'POST', body: data });
  },
  // ... add other HTTP methods (put, delete, patch) as needed
  
  // Method to manage interceptors
  interceptors: {
    request: {
      use: (fulfilled, rejected) => {
        _axios.requestInterceptors.push(fulfilled);
      },
    },
    response: {
      use: (fulfilled, rejected) => {
        _axios.responseInterceptors.push({ fulfilled, rejected });
      },
    },
  },
};


// --- 2. Interceptor Logic (Modified to use the new axios structure) ---

// Add a request interceptor
_axios.interceptors.request.use(
  function(config) {
    // Do something before request is sent
    return config;
  },
  function(error) {
    // Do something with request error
    return Promise.reject(error);
  }
);

// Add a response interceptor
_axios.interceptors.response.use(
  function(response) {
    // Do something with response data
    return response;
  },
  function(error) {
    // Do something with response error
    // Note: The error object now contains the HTTP response object in error.response
    return Promise.reject(error);
  }
);


// --- 3. Vue Plugin Installation ---

const Plugin = {};

Plugin.install = function(Vue, options) {
  // Bind the custom axios wrapper to Vue
  Vue.axios = _axios;
  window.axios = _axios; // Overwriting window.axios is generally discouraged but kept for parity with original axios code

  Object.defineProperties(Vue.prototype, {
    axios: {
      get() {
        return _axios;
      }
    },
    $axios: {
      get() {
        return _axios;
      }
    },
  });
};

Vue
