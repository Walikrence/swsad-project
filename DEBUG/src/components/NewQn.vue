<template>
<div>
  <div class="qn-container">
    <div class="qn-cell">
      <span>标题： </span>
      <input type="text">
    </div>
    <div class="qn-cell" v-for="q in qn" :key='q'>
      {{q}}
    </div>
    <a-button type="primary">创建问卷</a-button>
  </div>
</div>
</template>

<script>
// import axios from 'axios'

export default {
  data: function () {
    return {
      qn: {
        title: null,
        q: {
          singleQ: null,
          multiQ: null,
          textQ: null
        }
      },
      qnn: [1, 2, 3]
    }
  },
  methods: {
  }
}
</script>

<style scoped>
.qn-container {
  margin-left: calc(50vw - 300px);
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
  border: 1px solid red;
}

.qn-cell>input {
  border-left: none;
}
</style>
