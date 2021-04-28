<template>
  <div class="container">
    <h2>性别分布</h2>
    <div class="charts"><ve-ring :data="chartData"></ve-ring></div>

  </div>

</template>

<script>
export default {
  data() {
    return {
      chartData: {
        columns: ['性别', '人数'],
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
          .get(`/charts/getSex`)
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
  margin-top: 100px;
}
</style>