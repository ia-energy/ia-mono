module.exports = {
  devServer: {
    https: false,
    proxy: {
      "/api": {
        target: "http://ia-flask:5000"
      }
    },
  }
}
