<template>
<div class="container">
  <el-card shadow="hover" v-for="item in jiekous">
    <div slot="header" class="header">
      <span>{{item.title}}</span>
      <el-button type="success" style="float: right" @click="start(item.url,item.data)">开始</el-button>
    </div>
    <div>
      <h3>地址：</h3>
      <p>{{item.url}}</p>

      <h3>提交：</h3>
      <p>{{item.data|JsonFilter}}</p>
      <h3>期望：</h3>
      <p>{{item.wish|JsonFilter}}</p>

      <h3>返回：</h3>
      <p>状态：{{res.status}}</p>
      <p>数据：{{res.data|JsonFilter}}</p>
    </div>
  </el-card>
</div>
</template>

<script>
import config from "@/components/test/config";

export default {
  data(){
    return {
      jiekous:config,


      res:{},
    }
  },
  filters:{
    JsonFilter(obj){
      return JSON.stringify(obj)
    },
  },
  created() {

  },

  methods:{
    start(url,data){
      this.test(url,data)
    },
    test(url,data){
      this.$http
          .post(url, data)
          .then(res => {
            this.res = res

          })
          .catch(error => {
            this.res = error
            console.log(error);
          });
    },


  }

}
</script>

<style scoped>
.container{
  padding-left: 200px;
  padding-right: 200px;
  padding-top: 100px;
}
.el-card{
  background-color: #E6E5E5;
}
h3{
  color: red;
}
.header span{
  color: blue;
  font-size: 20px;
}
</style>