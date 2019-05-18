module.exports = {
	// 指定`build`时,在静态文件上一层添加static目录
	assetsDir: 'static',
	// ant-design config
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
};