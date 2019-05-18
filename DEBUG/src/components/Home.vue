<template>
<div>
  <div class="banner-container">
   <div class="banner-cell banner-new-qn" @click="newQnClick">创建空白问卷</div>
   <div class="banner-cell banner-new-qn1">选择问卷模板</div>
   <div class="banner-cell banner-new-qn2">文本编辑问卷</div>
  </div>
  <div class="bottom-container">
   <div>copyright fangege</div>
  </div>
</div>
</template>

<script>
// import axios from 'axios'

export default {
  data: function () {
    return {
    }
  },
  methods: {
    newQnClick: function () {
      this.$router.push({ path: '/guide/newQn' })
    }
  }
}
</script>

<style scoped>
.banner-container {
}

.banner-cell {
  float: left;
  width: 33.3%;
  height: 500px;
  line-height: 500px;
  text-align: center;
  font-size: 24px;
  color: white;
}

.banner-new-qn {
  background-color: rgba(46, 140, 219, 0.95);
}

.banner-new-qn1 {
  background-color: rgba(71, 157, 230, 0.97);
}

.banner-new-qn2 {
  background-color: rgba(144, 214, 126, 0.94);
}

.bottom-container {
  text-align: center;
  font-size: 14px;
}

.button-sign:hover {
  background-color: var(--cyan-hover);
  cursor: pointer;
}
</style>
