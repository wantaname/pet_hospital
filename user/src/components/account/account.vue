<template>
  <div class="container">
    <el-row>
      <el-col :span="3" :offset="2">
        <div class="menu">
          <el-menu
              default-active="1"
              class="el-menu-vertical-demo"
              router
          >
            <el-menu-item index="userInfo">
              <i class="el-icon-menu"></i>
              <span slot="title">账号信息</span>
            </el-menu-item>
            <el-menu-item index="examInfo">
              <i class="el-icon-document"></i>
              <span slot="title">考试记录</span>
            </el-menu-item>
            <el-menu-item index="scoreAnalysis">
              <i class="el-icon-coin"></i>
              <span slot="title">分数排行</span>
            </el-menu-item>

            <el-menu-item index="login">
              <i class="el-icon-user"></i>
              <span slot="title">退出登录</span>
            </el-menu-item>

          </el-menu>
        </div>
      </el-col>

      <el-col :span="16">
        <div class="main">
          <router-view></router-view>
        </div>
      </el-col>

    </el-row>


    </div>

</template>

<script>
export default {
  data() {
    return {}
  },

  created() {


  },
  methods: {}

}
</script>

<style scoped>
.container {
  height: 100%;
  /*margin-top: 28px;*/
}

.menu {

  overflow: hidden;
}

.menu .el-menu {
  margin-top: 100px;
  padding-top: 60px;
  height: 350px;
  border-radius: 40px;
  background-color: rgba(255, 255, 255, 0.5);

}

.main {
  margin-left: 20px;
  padding-top: 40px;
  height: 580px;
  border-radius: 10px;

}


</style>