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
    <a-button type="primary" class="new-qn-button" @click="editQn">修改问卷</a-button>
  </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
  data: function () {
    return {
      qn: {
        title: null,
        q: [
          {type: 'single', name: 'sn', cnum: 3, choices: ['c1', 'c2', 'c3']},
          {type: 'multi', name: 'mn', cnum: 3, choices: ['c11', 'c22', 'c33']},
          {type: 'text', name: 'name'}
        ]
      }
    }
  },
  methods: {
    addSingle: function () {
      this.qn.q.push({type: 'single', name: '', cnum: 1, choices: []})
    },
    addMulti: function () {
      this.qn.q.push({type: 'multi', name: '', cnum: 1, choices: []})
    },
    addText: function () {
      this.qn.q.push({type: 'text', name: ''})
    },
    removeQ: function (i) {
      this.qn.q.splice(i, 1)
    },
    editQn: function () {
      axios
        .post('/papers/editpaper', {
          paper: this.qn
        })
        .then((response) => {
          console.log(response)
        })
        .catch((error) => alert(error))
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
  width: 60px;
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
