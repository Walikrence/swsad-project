<template>
<div>
  <div class="banner-cell banner-qn" @click="qnClick">
    问卷系统
  </div>
  <div class="banner-cell banner-qn" @click="taskClick">
    小任务系统
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
.banner-cell {
  float: left;
  width: 400px;
  height: 450px;
  margin-top: calc((100vh - 510px)/2);
  margin-left: calc((100vw - 800px)/3);
  line-height: 450px;
  text-align: center;
  font-size: 24px;
  color: white;
  /*radius*/
  border-radius: 10px;
  transition: 0.3s;
}

.banner-cell:hover {
  cursor: pointer;
  transform: translate(-1px, -3px);
  box-shadow: 0 3px 3px var(--grey-shadow);
}

.banner-qn {
  background-color: rgba(46, 140, 219, 0.95);
}

.banner-task {
  background-color: rgba(71, 157, 230, 0.97);
}
</style>
