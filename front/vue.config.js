module.exports = {
  devServer: {    
    host: '0.0.0.0',
    port: 8080,
    public: 'to.me',
    disableHostCheck: true,
    proxy : 'https://github.com/'
  },
}