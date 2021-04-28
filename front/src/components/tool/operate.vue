<template>
  <div class="container">
    <el-card shadow="hover">
      <div slot="header">
        <span class="title">操作记录</span>
        <el-input placeholder="请输入内容" v-model="keyword" class="search">
          <el-select v-model="column" slot="prepend" placeholder="请选择">
            <el-option label="用户名" value="username"></el-option>
            <el-option label="操作类型" value="type"></el-option>
            <el-option label="数据表" value="table"></el-option>
            <el-option label="操作时间" value="op_time"></el-option>
          </el-select>
          <el-button slot="append" icon="el-icon-search" @click="clickSearch"></el-button>
        </el-input>
      </div>
      <el-table
          :data="tableData"
          stripe
          style="width: 100%">

        <el-table-column
            prop="username"
            label="用户名"
        >
        </el-table-column>
        <el-table-column
            prop="type"
            label="操作类型"
        >
        </el-table-column>

        <el-table-column
            prop="table"
            label="数据表"
        >
        </el-table-column>

        <el-table-column
            label="操作时间"
        >
          <template slot-scope="scope">
            <i class="el-icon-time"></i>
            <span style="margin-left: 10px">{{ scope.row.op_time }}</span>
          </template>

        </el-table-column>
      </el-table>


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
</template>

<script>
export default {
  data() {
    return {
      //  表格数据
      tableData: [],
      //编辑


      keyword: "",
      column: "username",
      //  分页
      page:{
        pagenum:1,
        pagesize:10,
        total:0
      }

    }
  },
  created() {
    //  获取数据
    this.getData()
  },

  methods: {

    //点击搜索
    clickSearch(){
      this.getData()
    },

    getData() {
      this.$http
          .get(`/user/record`,{
            params:{
              keyword: this.keyword,
              column: this.column,
              pagenum: this.page.pagenum,
              pagesize: this.page.pagesize,
            }
          })
          .then(res => {
            if (res.status !== 200) return this.message.error("获取信息失败!");

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
.search{
  width: 40%;
  margin-left: 50px;
}
.title{
  color: #11ABF8;
}
</style>