<template>
<div>
  <div class="task-container">
    显示任务详情
    <a-button type="primary" class="accept-task-button" @click="acceptTask">接受任务</a-button>
  </div>
</div>
</template>

<script>
export default {
  data: function () {
    return {
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

.task-input {
  display: inline-block;
  margin-top: 10px;
  width: 300px;
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
