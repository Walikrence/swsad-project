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
      <a-list-item slot="renderItem" slot-scope="item">
        <a-card hoverable :title="item.title" @click="editQnClick(item)">
          <!-- <img alt="qncover" src="@/assets/qncover.jpg" slot="extra" class="card-cover"/> -->
          <span class="list-card-time">创建者: {{item.creater}}</span>
          <span class="list-card-name">创建时间: {{tmpqninfo1}}</span>
        </a-card>
      </a-list-item>
    </a-list>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

export default {
  data: function () {
    return {
      qnList: [],
      tmpqninfo1: '2019-05-25'
    }
  },
  created: function () {
    axios
      .post('/api/paper/query/', {
        username: this.userInfo
      })
      .then((response) => {
        var resp = response.data
        // console.log(JSON.stringify(resp.paper_list))
        if (resp.code === 2) { // success
          for (let i = 0; i < resp.paper_list.length; i++) {
            let q = resp.paper_list[i]
            if (q.creater === this.userInfo) {
              this.qnList.push(q)
            }
          }
        }
      })
      .catch((error) => this.$message.error(error))
  },
  computed: {
    ...mapState(['userInfo'])
  },
  methods: {
    newQnClick: function () {
      this.$router.push({ path: '/guide/newQn' })
    },
    editQnClick: function (qn) {
      // console.log(qn)
      this.$router.push({
        // path: '/guide/editQn',
        name: 'editQn',
        params: {
          qn: qn
        }
      })
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
