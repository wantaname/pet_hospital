<template>
  <div class="container">
    <el-row>
      <el-col :span="3" :offset="2">

        <el-card shadow="hover">
          <div slot="header" class="clearfix">
            <span style="color: blue">考试信息</span>

          </div>
          <div class="left">
            <div class="time">
              <span style="font-weight: bold">考试时间</span>: <span style="color: red">{{ examInfo.exam_time }}</span>
            </div>
            <div>
              <span style="font-weight: bold">用时</span><span style="color: red">：{{ examInfo.use_time }}</span>
            </div>
            <div>
              <span style="font-weight: bold">分数</span><span style="color: red">：{{ examInfo.total_score }}</span>
            </div>
          </div>
        </el-card>

        <div class="back">
          <el-button type="success" @click="back">返回</el-button>
        </div>
      </el-col>

      <el-col :span="16" :offset="1" class="exam_col">
        <el-card class="exam_card" shadow="hover">


          <div slot="header" class="clearfix">
            <span style="color: blue">答卷</span>
            <span style="color: orange;float: right">每题4分，共{{Number(this.examData.length)*4}}分</span>
          </div>
          <div class="content">
            <div v-for="(item,index) in examData">
              <p><span>{{ index + 1 }}. </span>{{ item.question }} <span style="color: red">{{ item.result }}</span></p>

              <el-radio v-model="item.answer" :label="option" border v-for="option in item.options"
                        :key="String(index)+option" disabled>{{ option }}
              </el-radio>
              <p class="solution">
                <span style="color: darkorange">正确答案：</span><span style="color: blue">{{ item.solution }}</span>
              </p>
              <p class="jiexi" style="color: red">
                解析：<span style="color: blue">{{ item.note|jiexi }}</span>
              </p>
              <el-divider></el-divider>
            </div>

          </div>


        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      examId: 1,
      percentage: 0,
      examData: [
        {
          id: "id", username: "username", question_id: "question_id", question: "question", options: [],
          answer: "answer", result: "result", solution: "solution", note: "note", score: 'score'
        }
      ],
      examInfo: {
        "total_score": 0,
        "use_time": "00 : 00 : 00",
        "exam_time": "1900-01-01",
      }
    }
  },
  created() {
    this.getData()

  },
  filters: {

    jiexi(note) {
      if (note) {
        return note
      } else {
        return "暂无解析。"
      }
    }
  },
  methods: {
    back() {
      this.$router.push("/examInfo")

    },
    getData() {
      this.examId = this.$route.query.examId

      let data = {examId: this.examId}
      this.$http
          .post("/pet_exam/getExam", data)
          .then(res => {

            if (res.data.status == 404) {
              this.$message.error("用户未登录");

            } else if (res.data.status == 300) {

              return this.$message.error(res.data.msg)
            } else if (res.data.status == 200) {
              // this.work = work

              this.examData = res.data.examData.data
              this.examInfo = res.data.examData.info


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
  overflow: auto;

}

.el-row {
  margin-top: 20px;
  height: calc(100% - 20px);
}

.exam_col {
  height: 100%;
  overflow: auto;
}

.left div{
  margin-top: 20px;
  margin-bottom: 20px;
}
.back{
  padding-left: 20px;
  padding-top: 30px;
}
</style>