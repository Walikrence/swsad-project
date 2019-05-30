<template>
<div>
  <div class="header-container">
    <span class="header-title">全部问卷</span>
  </div>
  <div class="list-container">
    <a-list itemLayout="vertical" size="large" :dataSource="qnList">
      <a-list-item slot="renderItem" slot-scope="item, index">
        <a-card hoverable :title="item.title" @click="fillQnClick(item)">
          <span class="list-card-time">{{tmpqninfo1}}</span>
          <span class="list-card-name">{{tmpqninfo2}}</span>
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
      qnList: [
        {
          title: '这是问卷1',
          q: []
        },
        {
          title: '这是问卷2',
          q: []
        },
        {
          title: '这是问卷3',
          q: []
        },
        {
          title: '这是问卷4',
          q: []
        },
        {
          title: '这是问卷5',
          q: []
        }
      ],
      tmpqninfo1: '创建时间: 2019-05-25',
      tmpqninfo2: '创建者: kris wu'
    }
  },
  methods: {
    fillQnClick: function (qn) {
      console.log(qn)
      this.$router.push({ path: '/guide/fillQn' })
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
