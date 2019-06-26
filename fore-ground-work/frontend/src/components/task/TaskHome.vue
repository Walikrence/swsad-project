<template>
<div>
  <div class="banner-container">
    <div class="banner-cell banner-task1" @click="taskClick">
      <a-icon class="banner-icon" type="plus-square" />
      校园互助任务
    </div>
    <div class="banner-cell banner-task2" @click="tradeClick">
      <a-icon class="banner-icon" type="diff" />
      校园交易站
    </div>
  </div>
  <div class="bottom-container">
    <!-- <div>copyright</div> -->
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
    taskClick: function () {
      this.$router.push({ path: '/guide/taskList' })
    },
    tradeClick: function () {
    }
  }
}
</script>

<style scoped>
.banner-container {
}

.banner-cell {
  float: left;
  width: 50%;
  height: 500px;
  line-height: 500px;
  text-align: center;
  font-size: 24px;
  color: white;
}

.banner-cell:hover {
  cursor: pointer;
}

.banner-task1 {
  background-color: rgba(46, 140, 219, 0.95);
}

.banner-task2 {
  background-color: rgba(144, 214, 126, 0.94);
}

.banner-icon {
  display: inline-block;
  font-size: 60px;
}

.bottom-container {
  text-align: center;
  font-size: 14px;
}
</style>
