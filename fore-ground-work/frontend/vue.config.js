const path = require('path')

module.exports = {
	devServer: {
		proxy: {
	      '/api': {
	        target: 'http://localhost:8080',
	        pathRewrite: {'^/api' : ''}
	      }
	    }
	},
	chainWebpack: (config) => {
		config.resolve.alias
			.set('@', path.join(__dirname, 'src'))
	},
  assetsDir: 'static',
  css: {
    loaderOptions: {
      less: {
        modifyVars: {
          'primary-color': '#199ED8',
          'link-color': '#1DA57A',
          'border-radius-base': '2px',
        },
        javascriptEnabled: true
      }
    }
  }
}