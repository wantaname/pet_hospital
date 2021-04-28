<template>
<div class="container">
  <el-card class="box-card" shadow="hover">
    <div slot="header" class="clearfix">
      <h3>百度文库</h3>
    </div>
    <div>
      <div class="row">
      <span class="item">请求方法：</span><span>POST</span>
      </div>

      <div class="row">
        <span class="item">请求地址：</span><span>http://47.100.77.177:6666/download</span>
      </div>

      <div class="row">
        <span class="item">请求参数：</span>
        <ul>
          <li>url: 文库链接</li>
          <li>username: 用户名</li>
          <li>password: 密码</li>
        </ul>
      </div>

      <div class="row">
        <span class="item">返回数据：</span>
        <ul>
          <li>status: 状态</li>
          <li>msg: 消息</li>
          <li>ddl_url: 下载地址</li>
        </ul>
      </div>
    </div>
  </el-card>
</div>
</template>

<script>
export default {
  name: "api"
}
</script>

<style scoped>
.el-card{
  margin-top: 40px;
  background-color: #F8F8F9;
}

.row{
  margin: 12px 5px;
}

.item{
  color: red;
}
</style>