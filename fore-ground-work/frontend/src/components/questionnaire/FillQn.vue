<template>
<div>
  <div class="qn-title-container">
    <div class="qn-title-text">{{qn.title}}</div>
    <div class="qn-title-hint">{{hint}}</div>
  </div>
  <div class="qn-container">
    <a-progress class="progress-container" :percent="progressPercent" :showInfo="true" />
    <!-- 问题列表 -->
    <div class="qn-cell" v-for="(q, i) in qn.q" :key="i">
      <!-- 单选题 -->
      <div v-if="q.type=='single'">
        <div class="qn-title">{{i+1}}. {{q.name}}</div>
        <a-radio-group v-model="q.answer">
          <a-radio class="qn-choice" v-for="j in q.cnum" :key="j" :value="q.choices[j-1].text" >{{q.choices[j-1].text}}</a-radio>
        </a-radio-group>
      </div>
      <!-- 多选题 -->
      <div v-else-if="q.type=='multi'">
        <div class="qn-title">{{i+1}}. {{q.name}}</div>
        <a-checkbox-group v-model="q.answer">
          <a-checkbox class="qn-choice" v-for="j in q.cnum" :key="j" :value="q.choices[j-1]">{{q.choices[j-1].text}}</a-checkbox>
        </a-checkbox-group>
      </div>
      <!-- 填空题 -->
      <div v-if="q.type=='text'">
        <div class="qn-title">{{i+1}}. {{q.name}}</div>
        <a-input class="qn-input" v-model="q.answer" />
      </div>
    </div>
    <!-- 问题列表结束 -->
    <a-button type="primary" class="new-qn-button" @click="fillQn">提交</a-button>
  </div>
</div>
</template>

<script>
// import axios from 'axios'

export default {
  data: function () {
    return {
      qn: {
        title: '最喜欢的乐队调查',
        id: null,
        q: [
          // { type: 'single', name: '你平时听歌的频率', cnum: 3, choices: ['每天', '每周一到两次', '更少'], answer: null },
          // { type: 'multi', name: '你平时听以下哪些歌手的音乐', cnum: 5, choices: ['林宥嘉', '林俊杰', 'Oasis', 'The Cranberries', '吴亦凡'], answer: null },
          // { type: 'single', name: '你是否购买过实体专辑', cnum: 2, choices: ['是', '否'], answer: null },
          // { type: 'single', name: '你是否购买过数字专辑', cnum: 2, choices: ['是', '否'], answer: null },
          // { type: 'text', name: '你最喜欢的歌手', answer: null }
        ]
      },
      hint: '为了给您提供更好的服务，希望您能抽出几分钟时间，将您的感受和建议告诉我们，我们非常重视每位用户的宝贵意见，期待您的参与！现在我们就马上开始吧！'
    }
  },
  created: function () {
    var tQn = this.$route.params.qn
    // console.log(JSON.stringify(tQn))
    // parse quiestionnaire to qn format below
    this.qn.title = tQn.title
    this.qn.id = tQn.id
    var tQ
    for (let i = 0; i < tQn.Question_select.length; i++) { // select questions
      tQ = tQn.Question_select[i]
      var q = {
        type: tQ.mytype === '单选' ? 'single' : 'multi',
        name: tQ.title,
        id: tQ.id,
        cnum: tQ.option_num,
        choices: [],
        answer: null
      }
      for (let j = 0; j < tQ.option.length; j++) {
        q.choices.push({
          text: tQ.option[j].text,
          id: tQ.option[j].id,
          select: false
        })
      }
      this.qn.q.push(q)
    }
    for (let i = 0; i < tQn.Question_fill.length; i++) { // fill questions
      tQ = tQn.Question_fill[i]
      this.qn.q.push({
        type: 'text',
        name: tQ.title,
        id: tQ.id,
        answer: null
      })
    }
  },
  methods: {
    fillQn: function () {
      console.log(JSON.stringify(this.qn))
    }
  },
  computed: {
    progressPercent: function () {
      var totalNum = this.qn.q.length
      var answerNum = 0
      for (var i = 0; i < totalNum; i++) {
        if (this.qn.q[i].answer != null && this.qn.q[i].answer !== '') {
          answerNum++
        }
      }

      return parseInt(answerNum / totalNum * 100)
    }
  }
}
</script>

<style scoped>
.qn-title-container {
  margin-left: calc(50vw - 300px);
  margin-top: 20px;
  width: 600px;
  text-align: center;
}

.qn-title-text {
  margin-top: 40px;
  font-size: 30px;
  font-weight: bolder;
}

.qn-title-hint {
  margin-top: 20px;
  font-size: 16px;
}

.qn-container {
  margin-left: calc(50vw - 300px);
  margin-top: 40px;
  margin-bottom: 20px;
  width: 600px;
  text-align: center;
  padding: 20px 30px 30px 30px;
  background-color: white;
  /*radius*/
  border-radius: 3px;
  /*shadow*/
  box-shadow: -1px 1px 5px var(--grey-shadow);
}

.qn-cell {
  margin-top: 40px;
  text-align: left;
}

.qn-title {
  font-size: 18px;
  font-weight: bold;
}

.qn-choice {
  display: block;
  margin-top: 20px;
  margin-left: 8px;
  font-size: 16px;
}

.qn-input {
  margin-top: 20px;
}

.new-qn-button {
  margin-top: 20px;
}
</style>
