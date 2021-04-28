<template>
  <div class="container">
    <div v-if="!view">
      <el-card shadow="hover">
        <div slot="header">
          <span class="title">各省新增</span>

          <el-input placeholder="请输入内容" v-model="keyword" class="search">
            <el-select v-model="column" slot="prepend" placeholder="请选择">
              <el-option label="全部" value="all"></el-option>
              <el-option label="日期" value="date"></el-option>
              <el-option label="省份" value="province"></el-option>
              <el-option label="确诊人数" value="confirmed"></el-option>
              <el-option label="疑似人数" value="suspected"></el-option>
              <el-option label="治愈人数" value="cured"></el-option>
              <el-option label="死亡人数" value="dead"></el-option>
            </el-select>
            <el-button slot="append" icon="el-icon-search" @click="clickSearch"></el-button>
          </el-input>

          <el-button @click="clickView" type="text" icon="el-icon-view"
                     style="font-size: 28px;float:right"></el-button>


        </div>

        <el-table

            :data="tableData"
            stripe

            style="width: 100%">
          <!--    多选-->

          <el-table-column
              prop="id"
              label="id"
          >
          </el-table-column>


          <el-table-column
              prop="date"
              label="日期"
          >
            <template slot-scope="scope">
              <i class="el-icon-time"></i>
              <span style="margin-left: 10px">{{ scope.row.date }}</span>
            </template>

          </el-table-column>

          <el-table-column
              prop="province"
              label="省份">
          </el-table-column>

          <el-table-column
              prop="confirmed"
              label="确诊">
          </el-table-column>
          <el-table-column
              prop="suspected"
              label="疑似">
          </el-table-column>
          <el-table-column
              prop="cured"
              label="治愈">
          </el-table-column>
          <el-table-column
              prop="dead"
              label="死亡">
          </el-table-column>


        </el-table>

        <!--    分割线-->
        <el-divider></el-divider>

      </el-card>


      <!--    分页-->
      <!-- 分頁區 -->
      <el-pagination

          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="page.pagenum"
          :page-sizes="[5, 10,20,30]"
          :page-size="page.pagesize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="page.total"
      ></el-pagination>
    </div>

    <div v-else>
      <el-card shadow="hover">
        <div slot="header">
          <span class="title">各省新增</span>
          <el-input placeholder="请输入内容" v-model="vkeyword" class="search">
            <el-select v-model="vcolumn" slot="prepend" placeholder="请选择">
              <el-option label="省份" value="province"></el-option>
              <el-option label="日期" value="date"></el-option>
            </el-select>
            <el-button slot="append" icon="el-icon-search" @click="clickVsearch"></el-button>
          </el-input>

          <el-button @click="clickView" type="text" icon="el-icon-s-grid"
                     style="font-size: 28px;float:right"></el-button>

        </div>
        <div class="graph">
          <ve-line :data="chartData" v-if="vcolumn=='province'"></ve-line>
          <ve-histogram :data="chartData" v-else></ve-histogram>
        </div>
      </el-card>

    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      //图表数据
      chartData: {

      },
      //  表格数据
      tableData: [],
      //编辑

      view: false,

      //  搜索
      keyword: "",
      column: "all",

      vkeyword:"",
      vcolumn:"province",
      //  分页
      page: {
        pagenum: 1,
        pagesize: 10,
        total: 0
      }

    }
  },
  created() {
    //  获取数据
    this.getData()
  },
  methods: {

    clickView(){
      this.view=!this.view


    },
    clickVsearch(){
      //  获取图表数据
      this.$http
          .get(`/provinceIncrease/getChartData`, {
            params: {
              keyword: this.vkeyword,
              column: this.vcolumn,
            }
          })
          .then(res => {
            if (res.data.status == 404) {
              this.$message.error("用户未登录");

            }

            else if(res.data.status == 300)
            {

              return this.$message.error(res.data.msg)
            }
            else if (res.data.status == 200) {

              this.chartData = res.data.data
            }

          })
          .catch(error => {
            console.log(error);
          });
    },

    //点击搜索
    clickSearch() {
      this.getData()
    },


    //点击编辑
    handleEdit(index, row) {
      //打开对话框
      this.dialogVisible = true
      //根据id获得信息
      this.getPatientById(row.id)

    },


    getData() {
      this.$http
          .get(`/provinceIncrease/getData`, {
            params: {
              keyword: this.keyword,
              column: this.column,
              pagenum: this.page.pagenum,
              pagesize: this.page.pagesize,
            }
          })
          .then(res => {
            if (res.status !== 200) return this.message.error("获取患者信息失败!");

            this.tableData = res.data.data
            this.page.total = res.data.total
          })
          .catch(error => {
            console.log(error);
          });
    },

    //監聽pagesize改變的事件
    handleSizeChange(newSize) {
      this.page.pagesize = newSize;
      this.getData();
    },
    // 監聽頁碼值改變的事件
    handleCurrentChange(newPage) {
      this.page.pagenum = newPage;
      this.getData();
    }
  }
}
</script>

<style scoped>
.search {
  width: 40%;
  margin-left: 50px;
}


.title {
  color: #11ABF8;
}
</style>