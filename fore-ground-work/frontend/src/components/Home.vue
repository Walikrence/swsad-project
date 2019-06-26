<template>
<div>
  <a-carousel autoplay>
    <div class="carousel-container">
      <img class="carousel-img" src="@/assets/home-carousel-1.png">
      <div class="carousel-text">自定义问卷</div>
      <a-button class="carousel-button" type="primary" @click="qnClick">问卷调查</a-button>
    </div>
    <div class="carousel-container">
      <img class="carousel-img" src="@/assets/home-carousel-2.jpg">
      <span class="carousel-text">随时发布和获取任务</span>
      <a-button class="carousel-button" type="primary" @click="taskClick">小任务系统</a-button>
    </div>
    <div class="carousel-container">
      <img class="carousel-img" src="@/assets/home-carousel-3.jpg">
      <span class="carousel-text">社区系统</span>
    </div>
    <div class="carousel-container">
      <img class="carousel-img" src="@/assets/home-carousel-4.jpg">
      <span class="carousel-text">不只是问卷调查</span>
    </div>
  </a-carousel>
  <div class="description-container">
    <div class="description-title">他们正在使用</div>
    <div class="description-text">这是一个为大学生设计的平台，不仅仅可以在上面发表问卷</div>
    <div class="description-text">你还可以进行完成任务以及进行闲置物品交易</div>
  </div>
  <div class="detail-container">
    <div class="detail-content-container">
      <img class="detail-img" src="@/assets/home-detail-1.jpg">
      <div class="empty-block"></div>
      <div class="detail-content">
        <h1>在线编辑，操作简单</h1>
        <h3>• 提供问卷的在线编辑系统</h3>
        <h3>• 可以保存编辑的问卷，待需要时发布</h3>
        <h3>• 在线修改问卷</h3>
        <h3>• 实时悬赏</h3>
        <a-button class="detail-button" type="primary" @click="qnClick">点击进入问卷系统</a-button>
      </div>
    </div>
  </div>
  <a-divider class="detail-divider" />
  <div class="detail-container">
    <div class="detail-content-container">
      <div class="detail-content">
        <h1>任务系统，互帮互助</h1>
        <h3>• 在线发表任务需求</h3>
        <h3>• 发布方和接收方对接容易</h3>
        <h3>• 界面简单明了，易于查看</h3>
        <a-button class="detail-button" type="primary" @click="taskClick">点击进入小任务系统</a-button>
      </div>
      <div class="empty-block"></div>
      <img class="detail-img" src="@/assets/home-detail-2.jpg">
    </div>
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
    qnClick: function () {
      this.$router.push({ path: '/guide/qnHome' })
    },
    taskClick: function () {
      this.$router.push({ path: '/guide/taskHome' })
    }
  }
}
</script>

<style scoped>
.ant-carousel >>> .slick-slide {
  text-align: center;
  height: 400px;
  line-height: 400px;
  background: white;
  overflow: hidden;
}

.carousel-container {
  position: relative;
}

.carousel-img {
  /*object-fit:cover;*/
  /*min-width: 100%;*/
  /*min-height: 100%;
  width: auto;*/
  /*height: auto;*/
  /*max-width: 100%;
  max-height: 100%;
  height: inherit !important;*/
  /*object-fit: contain;*/
  width: 100%;
  height: auto;
  transform: translateY(-40%);
  -webkit-filter: brightness(.5);
}

.carousel-text {
  position: absolute;
  left: calc(50vw - 200px);
  top: -30px;
  width: 400px;
  text-align: center;
  font-size: 36px;
  font-weight: bold;
  color: #fff;
}

.carousel-button {
  position: absolute;
  left: calc(50vw - 60px);
  top: 230px;
  width: 120px;
  height: 40px;
  text-align: center;
  font-size: 16px;
  background-color: var(--yellow);
  border: none;
}

.carousel-button:hover {
  background-color: var(--yellow-hover);
}

.description-container {
  height: 300px;
  padding-top: 60px;
}

.description-title {
  margin-top: 20px;
  width: 100%;
  text-align: center;
  color: rgb(153, 153, 153);
  font-size: 24px;
}

.description-text {
  margin-top: 20px;
  width: 100%;
  text-align: center;
  color: black;
  font-size: 18px;
}

.detail-container {
  height: 300px;
  background-color: white;
}

.detail-content-container {
  width: 700px;
  height: 100%;
  margin: auto;
}

.detail-img {
  float: left;
  display: inline-block;
  height: 200px;
  margin-top: 50px;
}

.detail-content {
  float: left;
  display: inline-block;
  margin-top: 40px;
}

.empty-block {
  float: left;
  display: inline-block;
  width: 200px;
  height: 100%;
}

.detail-button {
  margin-top: 15px;
  width: 250px;
  height: 40px;
}

.detail-divider {
  margin: 0;
}
</style>
