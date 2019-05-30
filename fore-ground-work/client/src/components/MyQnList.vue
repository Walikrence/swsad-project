<template>
<div>
  <div class="header-container">
    <span class="header-title">我创建的问卷</span>
    <a-button type="primary" class="new-qn-button" @click="newQnClick">
      <a-icon type="plus" />创建问卷
    </a-button>
  </div>
  <div class="list-container">
    <a-list itemLayout="vertical" size="large" :dataSource="qnList">
      <a-list-item slot="renderItem" slot-scope="item, index">
        <a-card hoverable :title="item.title" @click="editQnClick(item)">
          <!-- <img alt="qncover" src="@/assets/qncover.jpg" slot="extra" class="card-cover"/> -->
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
          q: [
            // {type: 'single', name: 'sn', cnum: 3, choices: ['c1', 'c2', 'c3']},
            // {type: 'multi', name: 'mn', cnum: 3, choices: ['c11', 'c22', 'c33']},
            // {type: 'text', name: 'name'}
          ]
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
    newQnClick: function () {
      this.$router.push({ path: '/guide/newQn' })
    },
    editQnClick: function (qn) {
      console.log(qn)
      this.$router.push({ path: '/guide/editQn' })
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

.new-qn-button {
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
