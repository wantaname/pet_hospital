<template>
  <div class="container">

    <div v-loading="loading"
         element-loading-text="正在阅卷..."
         element-loading-spinner="el-icon-loading"
         element-loading-background="rgba(0, 0, 0, 0.8)" class="loading" v-if="loading"></div>

    <el-card class="start_card" v-if="state==='start'">
      <div slot="header" class="clearfix">
        <h2>考试须知</h2>
        <p>1. 考生须使用台式电脑或笔记本电脑进行考试，不支持手机或Pad等移动设备作答。</p>

        <p>2. 考试系统支持Windows和Mac OS系统。</p>

        <p>3. 请使用谷歌Chrome浏览器或360极速浏览器登录考试答题系统。</p>

        <p>4. 考生须保证电脑的摄像头、麦克风及扬声器等可以正常使用，保持电量充足。</p>

        <p>5. 网速要求：建议10Mbps以上（实际下载速度需达到1M/S）</p>

        <p>6. 开考前30分钟方可登录在线考试系统。迟到30分钟以上的考生不能登录在线考试系统。</p>

        <p>7. 考生请自行准备草稿纸和演算笔。</p>

        <p>8. 考试全程禁止佩戴耳机、口罩、帽子等，不得对面部进行遮挡并露出双耳。</p>

        <p>9. 考试过程中，每名考生离开考试答题界面不得超过5次。如遇断电、断网及硬件设备（如鼠标、键盘、显示器）故障等问题，请考生重新登录进行作答，系统不会停止计时，但已作答记录会全部保存。</p>

        <p>10. 考试过程中每名考生只允许登录一台电脑作答，中途不可更换设备。考试过程中需全程关闭微信、QQ、Team Viewer等聊天录屏远程软件。</p>


      </div>
      <div class="btn">
        <el-button type="success" @click="startExam">开始</el-button>
      </div>
    </el-card>

    <el-card class="exam_card" v-else-if="state==='exam'">
      <div class="right">
        <h2 class="time">
          <span>00 : {{ minute }} : {{ second }}</span>
        </h2>
        <div class="progress">
          <el-progress type="circle" :percentage="percentage"></el-progress>
        </div>
      </div>

      <div slot="header" class="clearfix">
        <span>试卷</span>
        <span style="color: orange;float: right">每题4分，共100分</span>
      </div>
      <div class="content">
        <div v-for="(item,index) in questions">
          <p><span style="color: orange">{{ index + 1 }}. </span>{{ item.Q }}</p>

          <el-radio v-model="item.answer" @click.native="check" :label="option" border v-for="option in item.A"
                    :key="String(item.id)+option">{{ option }}
          </el-radio>

        </div>

      </div>
      <el-divider></el-divider>
      <div class="submit">
        <el-button type="success" @click="submit">提交</el-button>
      </div>
    </el-card>

    <!--    结束-->
    <el-card class="over_card" v-if="state==='over'">
      <div slot="header" class="clearfix">
        <h2>考试结果</h2>
      </div>
      <div class="result">
        <p>答对<span>{{ yes }}</span>道，答错<span>{{ no }}</span>道,查看详情请
          <el-button type="primary" round @click="go">进入</el-button>
          个人中心
        </p>
      </div>
    </el-card>


  </div>
</template>

<script>
export default {
  data() {
    return {

      loading:false,
      state: "start",
      percentage: 0,
      questions: [
        {id: 1, Q: "问题", A: ["选项1", "选项2", "选项3", "选项4"], answer: ""},
        {id: 2, Q: "问题", A: ["选项1", "选项2", "选项3", "选项4"], answer: ""}
      ],
      time: 0,
      second: "0",
      minute: "0",
      yes: 0,
      no: 0,


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

    this.getData()


  },
  methods: {
    go(){
      this.$router.push("/examInfo")
    },
    startExam() {
      this.state = "exam";
      var _this = this
      setInterval(function () {
        _this.time += 1;
        let m = String(Math.round(_this.time / 60))
        if (m.length === 1) {
          _this.minute = "0" + m
        } else {
          _this.minute = m
        }
        let s = String(_this.time % 60)
        if (s.length === 1) {
          _this.second = "0" + s
        } else {
          _this.second = s
        }


      }, 1000)
    },
    check() {
      let count = 0;
      for (let item of this.questions) {
        if (item.answer !== "") {
          count += 1
        }
      }
      this.percentage = 4 * count
    },
    // 点击放大图片
    clickImg(img) {

    },
    submit(case_name) {
      this.loading = true
      this.currentCase = case_name;
      this.$http
          .post("/pet_exam/submit", {answers: this.questions, use_time: "00:" + this.minute + ":" + this.second})
          .then(res => {

            if (res.data.status == 404) {
              this.$message.error("用户未登录");

            } else if (res.data.status == 300) {

              return this.$message.error(res.data.msg)
            } else if (res.data.status == 200) {
              // this.work = work
              this.yes = res.data.yes;
              this.no = res.data.no;

              let _this = this
              setTimeout(function (){
                _this.loading = false
                _this.state = 'over'
              },3000)


            }
          })
          .catch(error => {

            console.log(error);
            return this.$message.error("系统错误！");

          });

    },

    getData() {
      let data = {}
      this.$http
          .post("/pet_exam/getData", data)
          .then(res => {

            if (res.data.status == 404) {
              this.$message.error("用户未登录");

            } else if (res.data.status == 300) {

              return this.$message.error(res.data.msg)
            } else if (res.data.status == 200) {
              // this.work = work

              this.questions = res.data.questions


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
  overflow: auto;

}

.right {
  width: 10%;
  position: fixed;
  top: 100px;
  right: 38px;
  color: red !important;
}

.process {
  display: flex;
  justify-content: center;
}

.el-progress__text {
  color: red;
}

.time {
  text-align: center;
}

.start_card h2 {
  color: red;
  text-align: center;
}

.start_card, .exam_card {
  width: 70%;
  margin: 10px auto;
}

.start_card {
  width: 60%;
}

.over_card {
  width: 40%;
  margin: 150px auto;
}

.over_card h2 {
  color: orange;
}

.result span {
  color: red;
}


.start_card .btn, .submit {
  display: flex;
  justify-content: center;
}

.content {
  padding: 20px 38px;
}

.loading{
  position: fixed;
  width: 100%;
  height: calc(100% - 60px);
  top: 60px;
  z-index: 300;
}
</style>