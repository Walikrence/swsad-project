<template>
<div>
  <div class="qn-type-container">
    <a-button type="dashed" class="qn-type-button" @click="addSingle" >
      <a-icon type="plus" />单选题
    </a-button>
    <a-button type="dashed" class="qn-type-button" @click="addMulti" >
      <a-icon type="plus" />多选题
    </a-button>
    <a-button type="dashed" class="qn-type-button" @click="addText" >
      <a-icon type="plus" />填空题
    </a-button>
  </div>
  <div class="qn-container">
    <div class="qn-cell">
      <div class="qn-title">问卷标题: </div>
      <a-input class="qn-input" v-model="qn.title" />
    </div>
    <!-- 问题列表 -->
    <div class="qn-cell" v-for="(q, i) in qn.q" :key="i">
      <!-- 单选题 -->
      <div v-if="q.type=='single'">
        <div class="qn-title">{{i+1}}. 单选题</div>
        <a-icon class="qn-delete-button" type="minus-circle-o" @click="removeQ(i)" />
        <div>
          <p class="qn-name">问题: </p><a-input class="qn-input" v-model="q.name" />
        </div>
        <div>
          <p class="qn-name">选项数: </p><a-input-number :min="1" :max="5" v-model="q.cnum" />
        </div>
        <div v-for="j in q.cnum" :key="j">
          <p class="qn-name">选项{{j}}: </p><a-input class="qn-input" v-model="q.choices[j-1]" />
        </div>
      </div>
      <!-- 多选题 -->
      <div v-else-if="q.type=='multi'">
        <div class="qn-title">{{i+1}}. 多选题</div>
        <a-icon class="qn-delete-button" type="minus-circle-o" @click="removeQ(i)" />
        <div>
          <p class="qn-name">问题: </p><a-input class="qn-input" v-model="q.name" />
        </div>
        <div>
          <p class="qn-name">选项数: </p><a-input-number :min="1" :max="5" v-model="q.cnum" />
        </div>
        <div v-for="j in q.cnum" :key="j">
          <p class="qn-name">选项{{j}}: </p><a-input class="qn-input" v-model="q.choices[j-1]" />
        </div>
      </div>
      <!-- 填空题 -->
      <div v-if="q.type=='text'">
        <div class="qn-title">{{i+1}}. 填空题</div>
        <a-icon class="qn-delete-button" type="minus-circle-o" @click="removeQ(i)" />
         <div>
          <p class="qn-name">问题: </p><a-input class="qn-input" v-model="q.name" />
        </div>
      </div>
    </div>
    <!-- 问题列表结束 -->
    <a-button type="primary" class="new-qn-button" @click="newQn">创建问卷</a-button>
  </div>
</div>
</template>

<script>
import axios from 'axios'

// debug axios
axios.interceptors.request.use(request => {
  console.log('Client Request Debug: ', request)
  return request
})

export default {
  data: function () {
    return {
      qn: {
        title: null,
        q: [
          // {type: 'single', name: 'sn', cnum: 3, choices: ['c1', 'c2', 'c3']},
          // {type: 'multi', name: 'mn', cnum: 3, choices: ['c11', 'c22', 'c33']},
          // {type: 'text', name: 'name'}
        ]
      }
    }
  },
  methods: {
    addSingle: function () {
      this.qn.q.push({ type: 'single', name: '', cnum: 1, choices: [] })
    },
    addMulti: function () {
      this.qn.q.push({ type: 'multi', name: '', cnum: 1, choices: [] })
    },
    addText: function () {
      this.qn.q.push({ type: 'text', name: '' })
    },
    removeQ: function (i) {
      this.qn.q.splice(i, 1)
    },
    newQn: function () {
      if (this.isNULL(this.qn.title)) { // empty title
        this.$message.warning('请填写问卷标题!')
        return
      }
      if (this.qn.q.length === 0) { // empty questions
        this.$message.warning('请至少添加一个问题')
        return
      }
      for (let i = 0; i < this.qn.q.length; i++) {
        let que = this.qn.q[i]
        if (this.isNULL(que.name)) { // empty question title
          this.$message.warning('问题' + (i + 1) + '的标题为空')
          return
        }
        if (que.type === 'text') { // input question
          continue
        }
        if (que.cnum !== que.choices.length) { // invalid choice num or empty
          this.$message.warning('问题' + (i + 1) + '的选项为空或选项数不匹配')
          return
        }
      }
      // valid, filter qn to JSON format
      // console.log(JSON.stringify(this.qn.q))
      var tSelectQ = []
      var tFillQ = []
      for (let i = 0; i < this.qn.q.length; i++) {
        let que = this.qn.q[i]
        let tque = {}
        if (que.type !== 'text') { // select question
          tque = {
            title: que.name,
            option_num: que.cnum,
            mytype: que.type === 'single' ? '单选' : '多选',
            option: []
          }
          for (let j = 0; j < que.choices.length; j++) {
            tque.option.push({ text: que.choices[j] })
          }
          tSelectQ.push(tque)
        } else { // fill question
          tque = {
            title: que.name
          }
          tFillQ.push(tque)
        }
      }
      // console.log(JSON.stringify(tSelectQ))
      // console.log(JSON.stringify(tFillQ))
      // post
      axios
        .post('/api/paper/create/', {
          title: this.qn.title,
          select_question_num: tSelectQ.length,
          fill_question_num: tFillQ.length,
          Question_select: tSelectQ,
          Question_fill: tFillQ
        })
        .then((response) => {
          var resp = response.data
          console.log(resp)
          if (resp.code === 3) { // success
            this.$message.success('创建问卷成功')
            this.$router.push({ path: '/guide/qnHome' })
          }
        })
        .catch((error) => this.$message.error(error))
    },
    isNULL: function (data) {
      if (data == null || data.length === 0) {
        return true
      }
      return false
    }
  }
}
</script>

<style scoped>
.qn-type-container {
  position: fixed;
  top: 80px;
  left: calc(50vw - 520px);
  width: 200px;
  padding: 0 20px 20px 20px;
  background-color: white;
  /*radius*/
  border-radius: 3px;
  /*shadow*/
  box-shadow: -1px 1px 5px var(--grey-shadow);
}

.qn-type-button {
  width: 160px;
  margin-top: 20px;
}

.qn-container {
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

.qn-cell {
  margin-top: 20px;
  text-align: left;
}

.qn-title {
  display: inline-block;
  width: 85px;
  font-size: 18px;
  font-weight: bold;
}

.qn-name {
  display: inline-block;
  margin-left: 20px;
  margin-top: 10px;
  width: 65px;
  font-size: 16px;
}

.qn-input {
  display: inline-block;
  margin-top: 10px;
  width: 300px;
}

.qn-delete-button {
  display: inline-block;
  font-size: 18px;
  color: red;
}

.new-qn-button {
  margin-top: 20px;
}
</style>
