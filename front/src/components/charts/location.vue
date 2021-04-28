<template>
  <div class="container">
    <h2>累计地图</h2>

    <div class="charts"> <ve-map :data="chartData"></ve-map></div>
  </div>

</template>

<script>
export default {
  data() {
    return {
      chartData: {
        columns: ['位置', '确诊',"疑似","治愈","死亡"],
        rows: [

        ]
      }
    }
  },
  created() {
    this.getData()
  },
  methods:{
    getData(){
      //  获取图表数据
      this.$http
          .get(`/charts/getMap`)
          .then(res => {
            if (res.data.status == 404) {
              this.$message.error("用户未登录");

            }

            else if(res.data.status == 300)
            {

              return this.$message.error(res.data.msg)
            }
            else if (res.data.status == 200) {

              this.chartData.rows = res.data.data
            }

          })
          .catch(error => {
            console.log(error);
          });
    }
  }

}
</script>
<style scoped>
h2{
  color: red;
}
.charts{
  width: 500px;
  margin: 10px auto;

}
</style>