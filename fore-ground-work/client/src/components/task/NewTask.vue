<template>
<div>
  <div class="task-container">
    <div class="task-cell">
      <div class="task-title">任务名称: </div>
      <a-input class="task-input" v-model="title" />
    </div>
    <div class="task-cell">
      <div class="task-title">联系方式: </div>
      <br>
      <div class="task-name">QQ: </div>
      <a-input class="task-input" v-model="qq" />
      <br>
      <div class="task-name">微信: </div>
      <a-input class="task-input" v-model="wechat" />
    </div>
    <div class="task-cell">
      <div class="task-title">任务信息: </div>
      <br>
      <div class="task-name">时间: </div>
      <a-input class="task-input" v-model="time" />
      <br>
      <div class="task-name">地点: </div>
      <a-input class="task-input" v-model="place" />
      <br>
      <div class="task-name">内容: </div>
      <a-input class="task-input" v-model="content" />
    </div>
    <div class="task-cell">
      <div class="task-title">任务报酬: </div>
      <a-input class="task-input" v-model="reward" />
    </div>
    <a-button type="primary" class="new-task-button">存为草稿</a-button>
    <a-button type="primary" class="new-task-button" @click="newTask">发布任务</a-button>
  </div>
</div>
</template>

<script>
export default {
  data: function () {
    return {
      title: null,
      qq: null,
      wechat: null,
      time: null,
      place: null,
      content: null,
      reward: null
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

.new-task-button {
  margin-top: 20px;
}
</style>
