<template>
  <div class="container">
    <el-card>
      <div class="avatar">
        <h3>头像</h3>
        <div class="upload_avatar">
          <el-upload
              ref="upload"
              drag
              :name="addInfo.filename"
              :action="upload_url"
              :auto-upload="true"

              :on-success="onUploaded"
          >
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          </el-upload>
        </div>
      </div>

      <div class="password">
        <h3>密码</h3>
        <div class="content">
          <div class="old">
            <span>旧密码：</span>
            <el-input v-model="password.oldValue" type="password" show-password></el-input>
          </div>
          <div class="new">
            <span>新密码：</span>
            <el-input v-model="password.newValue" type="password" show-password></el-input>
          </div>
          <el-button type="success" @click="submit">确定</el-button>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
import myconfig from "@/myconfig";

export default {
  data() {
    return {

      upload_url: myconfig.baseURL + "/pet/uploadAvatar",
      addAvatar_url: myconfig.baseURL + "/pet/addAvatar",
      username: "",
      addInfo: {
        filename: "",
      },
      password: {
        oldValue: "",
        newValue: "",
      }
    }
  },
  mounted() {

    // this.addInfo.filename = this.$root.$children[0].$children[0].username;
    this.getUserName();

  },
  methods: {

    submit() {
      if(this.password.newValue.length<5){
        return this.$message.warning("密码长度至少为5位！")
      }
      if(this.password.newValue===this.password.oldValue){
        return this.$message.warning("新旧密码相同！")
      }

      this.$http.post("/pet/modifyPassword", this.password).then(res => {
        if (res.data.status !== 200)
          return this.$message.error(res.data.msg);
        this.password.newValue = ""
        this.password.oldValue = ""
        this.$message.success(res.data.msg);
        this.$router.push("/login")
      }).catch(error => {
        console.log(error);
      });
    },
    //根据token获取用户名
    getUserName() {
      this.$http
          .get(`/pet/getUserName`)
          .then(res => {
            if (res.data.status !== 200) return this.message.error("获取登录信息失败!");
            if (res.data.username === "") {
              this.login()
            }
            this.username = res.data.username;

            this.addInfo.filename = this.username
          })
          .catch(error => {
            console.log(error);
          });
    },
    onUploaded(res) {
      console.log(res)
      if (res.status !== 200) {
        return this.$message.error(res.msg);
      } else {
        this.$http
            .post(this.addAvatar_url, {
              url: res.url,
            })
            .then(res => {

              if (res.data.status == 404) {
                this.$message.error("用户未登录");

              } else if (res.data.status == 300) {

                return this.$message.error(res.data.msg)
              } else if (res.data.status == 200) {
                this.$message.success("上传成功！")
                this.$refs.upload.clearFiles()

                // 父组件更新头像
                this.$root.$children[0].$children[0].getUserName();


              }
            })
            .catch(error => {

              console.log(error);
              return this.$message.error("系统错误！");

            });
      }
    },

  }


}
</script>

<style scoped>
.container {
  height: 100%;
}

h3 {
  color: orange;
}

.el-card {
  height: 100%;
}

.el-input {
  display: inline-block;
  width: 300px;
}

.password .content {
  padding-left: 50px;
}

.old, .new {
  margin-bottom: 20px;
}

.content button {
  margin-left: 60px;
}

</style>