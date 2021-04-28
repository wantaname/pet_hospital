<template>
  <div class="container">
    <el-row>

      <el-col :span="3" :offset="2">
        <div class="left">
          <el-steps :active="work_active" finish-status="success" direction="vertical" :space="88">
            <el-step :title="item.name" v-for="item in data" @click.native="changeWork(item.index)"></el-step>

          </el-steps>


        </div>
      </el-col>

      <el-col :span="14" class="c">
        <el-card shadow="hover" class="card" :body-style="{ padding: '0px' }">
          <div slot="header" class="clearfix">
            <div class="process">
              <el-steps :active="process_active" simple>
                <el-step :title="item.name" v-for="item in data[work_active].steps"></el-step>

              </el-steps>
            </div>
          </div>
          <div class="switch">
            <div class="previous">
              <el-button icon="el-icon-arrow-left" circle plain type="primary" @click="clickPrevious"></el-button>
            </div>
<!--            <img :src="data[work_active].steps[process_active].image" class="image">-->
            <el-image
                :src="data[work_active].steps[process_active].image"
                :preview-src-list="[data[work_active].steps[process_active].image]" class="img">
            </el-image>
            <div class="next">
              <el-button icon="el-icon-arrow-right" circle plain type="primary" @click="clickNext"></el-button>
            </div>
          </div>

          <div  class="detail">
            <span>{{ data[work_active].steps[process_active].text }}</span>
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
      work_active:0,
      process_active:0,
      data:[
        {index:0,name:"",steps:[{index:0,name:"",image:"",text:""}]}
      ]

    }
  },

  created() {

    this.getProcess()
  },
  methods: {
    changeWork(work_index){
      this.work_active = work_index
      this.process_active = 0
    },
    clickPrevious(){
      if(this.process_active<=0){

      }else {
        this.process_active--;
      }
    },
    clickNext(){
      if(this.process_active>=this.data[this.work_active].steps.length-1){
        this.process_active = 0
      }else {
        this.process_active++;
      }
    },
    getProcess(){
      let data = {}
      this.$http
          .post("/pet_cosplay/yishi", data)
          .then(res => {

            if (res.data.status == 404) {
              this.$message.error("用户未登录");

            } else if (res.data.status == 300) {

              return this.$message.error(res.data.msg)
            } else if (res.data.status == 200) {
              // this.work = work
              console.log(res.data.data)
              this.data = res.data.data

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
  margin-top: 28px;

}
.switch{
  display: flex;
  justify-content: space-around;
  align-items:center;
}
.image {
  height: 350px;
}
.card{
  position: fixed;
  width: 68%;
  padding-bottom: 30px;

}
.detail{

  padding: 10px 40px;
}

</style>