<template>
  <div class="container">
    <el-row>
      <el-col :span="6">
        <div class="left">
          <el-card shadow="hover">

            <div class="type" v-for="(item,index) in types">
              <h3>{{ item }}</h3>
              <div class="case_list">
                <el-button plain v-for="c in cases[index]" @click.native="selectCase(c)">{{ c }}</el-button>
              </div>
            </div>


          </el-card>
        </div>
      </el-col>

      <el-col :span="2" :offset="1">

        <div class="process">
          <el-steps :active="active" finish-status="success" direction="vertical" :space="88" class="steps">
            <el-step :title="item" v-for="(item,index) in process" @click.native="clickProcess(index)"></el-step>

          </el-steps>
        </div>
      </el-col>

      <el-col :span="15">
        <div class="right">
          <el-card shadow="hover" class="info_card">
            <div slot="header" class="clearfix">
              <span style="color: red">简介</span>
            </div>
            <div>
<!--              <img :src="caseInfo.info[0].image" alt="" v-if="caseInfo.info[0].image"-->
<!--                   @click="clickImg(caseInfo.info[0].image)">-->
              <el-image

                  :src="current[0].image"
                  :preview-src-list="[current[0].image,]" class="img">
              </el-image>
              <span>{{ current[0].text }}</span>
            </div>
          </el-card>

          <el-card shadow="hover" class="video_card" v-if="current[0].video!=''">
            <div slot="header">
              <span style="color:red;">视频</span>
            </div>
            <div v-html="caseInfo.info[0].video" class="video" v-if="current[0].video.indexOf('iframe')>-1">
              <!--              <img :src="caseInfo.info[0].image" alt="">-->

            </div>
            <div v-else class="video">
              <video :src="current[0].video" controls="controls">
                您的浏览器不支持 video 标签。
              </video>
            </div>

          </el-card>
        </div>

      </el-col>
    </el-row>


  </div>
</template>

<script>
export default {
  data() {
    return {

      active: 0,
      process: ["介绍", "接诊", "检查", "诊断结果", "治疗方案"],

      // 一一对应
      types: [],
      cases: [],

      currentCase: "犬瘟热",

      caseInfo: {
        info: [{case_name: "", text: "", image: "", video: ""}],
        receive: [{case_name: "", text: "", image: "", video: ""}],
        inspect: [{case_name: "", text: "", image: "", video: ""}],
        result: [{case_name: "", text: "", image: "", video: ""}],
        cure: [{case_name: "", text: "", image: "", video: ""}],
      },

      current: [{case_name: "", text: "", image: "", video: ""}],


    }
  },

  created() {

    this.getCase()
    this.selectCase(this.currentCase)

  },
  methods: {
    // 点击放大图片
    clickImg(img) {

    },
    selectCase(case_name) {
      this.active = 0
      this.currentCase = case_name;
      this.$http
          .post("/pet_case/getInfo", {"case": case_name})
          .then(res => {

            if (res.data.status == 404) {
              this.$message.error("用户未登录");

            } else if (res.data.status == 300) {

              return this.$message.error(res.data.msg)
            } else if (res.data.status == 200) {
              // this.work = work

              this.caseInfo = res.data.caseInfo
              console.log(this.caseInfo)


              if(this.active===0){
                this.clickProcess(0)
              }


            }
          })
          .catch(error => {

            console.log(error);
            return this.$message.error("系统错误！");

          });

    },
    clickProcess(work_index) {
      this.active = work_index
      console.log(this.active)
      // 接诊
      if(work_index===0){
        this.current = this.caseInfo['info']
      }
      else if(work_index===1){
          this.current = this.caseInfo['receive']
        console.log(this.current)
      }else if(work_index===2){
        this.current = this.caseInfo['inspect']
      }else if(work_index===3){
        this.current = this.caseInfo['result']
      }else if(work_index===4){
        this.current = this.caseInfo['cure']
      }
    },
    clickPrevious() {
      if (this.process_active <= 0) {

      } else {
        this.process_active--;
      }
    },
    clickNext() {
      if (this.process_active >= this.data[this.work_active].steps.length - 1) {
        this.process_active = 0
      } else {
        this.process_active++;
      }
    },
    getCase() {
      let data = {}
      this.$http
          .post("/pet_case/getCase", data)
          .then(res => {

            if (res.data.status == 404) {
              this.$message.error("用户未登录");

            } else if (res.data.status == 300) {

              return this.$message.error(res.data.msg)
            } else if (res.data.status == 200) {
              // this.work = work

              this.types = res.data.types
              this.cases = res.data.cases

            }
          })
          .catch(error => {

            console.log(error);
            return this.$message.error("系统错误！");

          });
    },
  }

}
</script>

<style scoped>
.container {

  height: 100%;
  /*margin-top: 28px;*/

}

.video_card .video {
  display: flex;
  justify-content: center;
}

.info_card .img {
  float: left;
  margin-right: 20px;
  width: auto!important;
  height: 380px !important;
  border-radius: 30px;

}

.left button {
  width: 150px;
  padding: 8px 10px;
  margin-right: 10px;
  margin-left: 0;
  margin-bottom: 10px;

}

.case_list {

}

.process {
  background-color: rgba(255, 255, 255, 0.5);
  position: fixed;
  top: 98px;
  padding-top: 38px;

  display: flex;
  justify-content: center;
  border-radius: 60px;
  color: red;
}

.el-row {
  height: 100%;
  /*overflow: auto;*/
}

.el-col {
  height: 100%;


}

.right {
  height: 100%;
  overflow: auto;
  padding-right: 40px;
}

.right .el-card {
  border-radius: 6px;
}

.steps {

}

.info_card, .video_card {
  margin-top: 30px;
  padding-bottom: 40px;
  background-color: rgba(208, 202, 200, 0.5);
}

.el-step {
  cursor: pointer;
}

.left h3 {
  color: rgb(51, 161, 209);
}

.left {
  position: sticky;
  top: -1px;
  height: 100%;
}

.left .el-card {

  height: 100%;
  background-color: rgb(243, 249, 235);
  overflow: auto;
}

.case_card {

}

.is-success {
  color: green !important;
}


</style>