let client;

export function setClient(newclient) {
  client = newclient;
}

// Request helpers
const reqMethods = [
    "request",
    "delete",
    "get",
    "$get",
    "head",
    "options", // url, config
    "post",
    "$post",
    "put",
    "$put",
    "patch",
    "$patch", // url, data, config
  ];

const service = {};

reqMethods.forEach((method) => {
  service[method] = function () {
    if (!client) {
      throw new Error("apiClient not installed");
    }
    return client[method].apply(null, arguments);
  };
});

export default service;