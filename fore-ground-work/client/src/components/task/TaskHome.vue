<template>
<div>
  <div class="banner-container">
    <div class="banner-cell banner-new-qn">
      <a-icon class="banner-icon" type="plus-square" />
      校园互助任务
    </div>
    <div class="banner-cell banner-new-qn1">
      <a-icon class="banner-icon" type="diff" />
      校园交易站
    </div>
    <div class="banner-cell banner-new-qn2" >
      <a-icon class="banner-icon" type="edit" />
      ---
    </div>
  </div>
  <div class="bottom-container">
    <!-- <div>copyright</div> -->
  </div>
</div>
</template>

<script>
// import axios from 'axios'

export default {
  data: function () {
    return {
    }
  },
  methods: {
  }
}
</script>

<style scoped>
.banner-container {
}

.banner-cell {
  float: left;
  width: 33.3%;
  height: 500px;
  line-height: 500px;
  text-align: center;
  font-size: 24px;
  color: white;
}

.banner-cell:hover {
  cursor: pointer;
}

.banner-new-qn {
  background-color: rgba(46, 140, 219, 0.95);
}

.banner-new-qn1 {
  background-color: rgba(71, 157, 230, 0.97);
}

.banner-new-qn2 {
  background-color: rgba(144, 214, 126, 0.94);
}

.banner-icon {
  display: inline-block;
  font-size: 60px;
}

.bottom-container {
  text-align: center;
  font-size: 14px;
}
</style>
