<template>
<div>
  <div class="task-container">
    <div class="task-cell">
      <div class="task-title">任务名称: </div>
      <span class="task-text">拿快递</span>
    </div>
    <div class="task-cell">
      <div class="task-title">联系方式: </div>
      <br>
      <div class="task-name">QQ: </div>
       <span class="task-text">454951085</span>
      <br>
      <div class="task-name">微信: </div>
       <span class="task-text">Vanrc0178</span>
    </div>
    <div class="task-cell">
      <div class="task-title">任务信息: </div>
      <br>
      <div class="task-name">时间: </div>
       <span class="task-text">周日下午</span>
      <br>
      <div class="task-name">地点: </div>
       <span class="task-text">明六</span>
      <br>
      <div class="task-name">内容: </div>
       <span class="task-text">京东快递，尾号8888</span>
    </div>
    <div class="task-cell">
      <div class="task-title">任务报酬: </div>
       <span class="task-text">10金币</span>
    </div>
    <a-button type="primary" class="accept-task-button" @click="acceptTask">接受任务</a-button>
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
    acceptTask: function () {
      this.$message.success('接受任务成功')
      this.$router.push({ path: '/guide/taskList' })
    }
  }
}
</script>

<style scoped>
.task-container {
  margin-left: calc(50vw - 300px);
  margin-top: 20px;
  margin-bottom: 20px;
  width: 600px;
  text-align: center;
  padding: 30px;
  background-color: white;
  /*radius*/
  border-radius: 3px;
  /*shadow*/
  box-shadow: -1px 1px 5px var(--grey-shadow);
}

.task-title {
  display: inline-block;
  width: 85px;
  font-size: 18px;
  font-weight: bold;
}

.task-cell {
  margin-top: 20px;
  text-align: left;
}

.task-text {
  display: inline-block;
  margin-left: 20px;
  font-size: 16px;
  font-weight: bold;
}

.task-name {
  display: inline-block;
  margin-left: 20px;
  margin-top: 10px;
  width: 65px;
  font-size: 16px;
}

.accept-task-button {
  margin-top: 20px;
}
</style>
