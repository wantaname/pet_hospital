<template>
  <el-container>

    <el-header>
      <el-menu
          :default-active="activeIndex"
          class="el-menu-demo"
          mode="horizontal"
          @select="handleSelect"
          router
      >

        <el-menu-item index="overview" class="overview">医院导览</el-menu-item>
        <el-submenu index="cosplay" class="cosplay">
          <template slot="title">角色扮演</template>
          <el-menu-item index="qiantai">前台</el-menu-item>
          <el-menu-item index="yizhu">医助</el-menu-item>
          <el-menu-item index="yishi">医师</el-menu-item>
        </el-submenu>
        <el-menu-item index="case" class="case">病例学习</el-menu-item>

        <el-menu-item index="exam" class="exam" >在线考试</el-menu-item>
        <el-menu-item index="account" class="account">
        <div class="login" v-if="username==''">
          <el-button type="success" @click="login">登录</el-button>
        </div>

        <div v-else>
          <el-avatar class="avatar" :src="avatar">
          </el-avatar>
          <span style="margin-left: 20px">{{username}}</span>
        </div>
        </el-menu-item>
      </el-menu>
    </el-header>
    <!-- 内容区域 -->
    <el-main>
      <div id="main">
        <router-view></router-view>
      </div>
    </el-main>


  </el-container>
</template>

<script>

import myconfig from "@/myconfig";

export default {

  data() {
    return {
      username:'',
      activeIndex: "1",
      avatar:myconfig.baseURL+"/static/image/default_avatar.png",
    };
  },
  created() {
    this.getUserName();
  },
  methods: {
    login(){
      this.$router.push("/login")
    },
    //根据token获取用户名
    getUserName(){

      this.$http
          .get(`/pet/getUserName`)

          .then(res => {
            console.log(res)
            if (res.status !== 200) return this.message.error("获取登录信息失败!");

            if(res.data.status!==200 || res.data.username===""){
              this.login()
              return
            }
            this.username = res.data.username
            console.log(res)
            if(res.data.avatar.indexOf("http")===-1){
              this.avatar = myconfig.baseURL+res.data.avatar
            }
            else {
              this.avatar = res.data.avatar
            }
            console.log(this.avatar)
          })
          .catch(error => {
            console.log(error);
          });
    },
    handleSelect(key, path) {
      console.log(key, path);
    }
  },

};
</script>

<style lang="less" scoped>
.el-container {
  height: 100%;
  background-image: url("./bg.jpg");
  background-size: 1566px;

}

.el-row {
  height: 100%;
}
#main{
  height: 100%;
}
.el-card {
  height: 100%;
}

.el-main {
  height: 100%;

  padding: 0;
  padding-top: 61px;
  overflow: hidden;
}

.el-header {
  position: fixed;
  width: 100%;
  padding: 0;
  height: 60px;
}
.account{
  float: right !important;
  margin-right: 10% !important;
}
.overview{
  margin-left: 10% !important;
}


</style>