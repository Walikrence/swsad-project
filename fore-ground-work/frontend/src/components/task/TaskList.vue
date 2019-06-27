<template>
<div>
  <div class="header-container">
    <span class="header-title">全部任务</span>
    <a-button type="primary" class="new-task-button" @click="newTaskClick">
      <a-icon type="plus" />发布任务
    </a-button>
  </div>
  <div class="list-container">
    <a-list itemLayout="vertical" size="large" :dataSource="taskList">
      <a-list-item slot="renderItem" slot-scope="item">
        <a-card hoverable :title="item.title" @click="taskClick(item)">
          <span class="list-card-time">{{tmptaskinfo1}}</span>
          <span class="list-card-name">{{tmptaskinfo2}}</span>
        </a-card>
      </a-list-item>
    </a-list>
  </div>
</div>
</template>

<script>
// import axios from 'axios'

export default {
  data: function () {
    return {
      taskList: [
        {
          title: '任务1',
          content: []
        },
        {
          title: '任务2',
          content: []
        },
        {
          title: '任务3',
          content: []
        },
        {
          title: '任务4',
          content: []
        },
        {
          title: '任务5',
          content: []
        }
      ],
      tmptaskinfo1: '发布人: 2019-05-25',
      tmptaskinfo2: '发布时间: kris wu'
    }
  },
  methods: {
    newTaskClick: function () {
      this.$router.push({ path: '/guide/newTask' })
    },
    taskClick: function (task) {
      // console.log(task)
      this.$router.push({ path: '/guide/taskDetail' })
    }
  }
}
</script>

<style scoped>
.header-container {
  width: 100%;
  height: 60px;
  top: 0;
  left: 0;
  line-height: 60px;
  background-color: white;
}

.header-title {
  margin-left: 40px;
  font-size: 20px;
  font-weight: bolder;
}

.new-task-button {
  float: right;
  margin-top: 12.5px;
  margin-right: 40px;
  width: 120px;
  height: 35px;
}

.list-container {
  margin: 20px;
}

.list-card-time {
  color: rgba(0, 0, 0, 0.45);
}

.list-card-name {
  margin-left: 20px;
  color: rgba(0, 0, 0, 0.45);
}
</style>
