<template>
<div>
  <div class="banner-container">
    <div class="banner-cell banner-new-qn" @click="newQnClick">
      <a-icon class="banner-icon" type="plus-square" />
      创建空白问卷
    </div>
    <div class="banner-cell banner-new-qn1" @click="fillQnClick">
      <a-icon class="banner-icon" type="diff" />
      填写问卷
    </div>
    <div class="banner-cell banner-new-qn2" @click="editQnClick">
      <a-icon class="banner-icon" type="edit" />
      编辑问卷
    </div>
  </div>
  <div class="bottom-container">
    <div class="bottom-title">随时挣闲钱</div>
    <hr class="bottom-divider" />
    <div class="bottom-text">填写问卷或发布你的问卷，完成调查的同时获得收益</div>
  </div>
</div>
</template>

<script>

export default {
  data: function () {
    return {
    }
  },
  methods: {
    newQnClick: function () {
      this.$router.push({ path: '/guide/newQn' })
    },
    fillQnClick: function () {
      this.$router.push({ path: '/guide/allQnList' })
    },
    editQnClick: function () {
      this.$router.push({ path: '/guide/myQnList' })
    }
  }
}
</script>

<style scoped>
.banner-container {
  height: 400px;
}

.banner-cell {
  float: left;
  width: 33.3%;
  height: 400px;
  line-height: 400px;
  text-align: center;
  font-size: 24px;
  color: white;
  transition: 0.3s;
}

.banner-cell:hover {
  cursor: pointer;
  /*transform: translate(-1px, -3px);*/
  transform: scale(1.001);
  box-shadow: 0 3px 3px var(--grey-shadow);
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

.banner-icon {
  display: inline-block;
  font-size: 60px;
}

.bottom-container {
  height: 300px;
  background-color: white;
  overflow: hidden;
}

.bottom-title {
  margin-top: 30px;
  margin-left: 60px;
  font-size: 18px;
}

.bottom-divider {
  margin: 20px 60px 20px 60px;
  /*color: rgb(240, 240, 240);*/
  background-color:  rgb(220, 220, 220);
  height: 2px;
  border:none;
}

.bottom-text {
  margin-top: 30px;
  margin-left: 60px;
  font-size: 16px;
}
</style>
