<template>
  <div id='app'>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  data: function () {
    return {}
  },
  /* 用localStorage解决vuex刷新丢失数据的问题 */
  created: function () {
    // 在页面加载时读取localStorage里的状态信息
    if (localStorage.getItem('store')) {
      this.$store.replaceState(Object.assign({}, this.$store.state, JSON.parse(localStorage.getItem('store'))))
    }
    // 在beforeunload页面刷新时将vuex里的信息保存到localStorage里
    window.addEventListener('beforeunload', () => {
      localStorage.setItem('store', JSON.stringify(this.$store.state))
    })
  }
}
</script>

<style>
:root {
  --blue: rgb(0, 132, 255);
  --blue-hover: rgb(15, 79, 207);
  --grey-menu: rgb(88, 88, 106);
  --grey-hover: rgb(210, 210, 210);
  --grey-shadow: rgb(190, 190, 190);
  --grey-background: rgb(240, 240, 240);
  --cyan: #199ED8;
  --cyan-hover: #2c8ab2;
  --yellow: #FF9900;
  --yellow-hover: #ffad32;
}

* {
  margin: 0;
  padding: 0;
}

body {
  width: 100%;
  height: 100%;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
  background-color: var(--grey-background);
  overflow: hidden;
}
</style>
