<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/' }">首頁</el-breadcrumb-item>
      <el-breadcrumb-item>項目數據</el-breadcrumb-item>
      <el-breadcrumb-item>譯語表</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 卡片 -->
    <el-card class="box-card">
      <el-row :gutter="2">
        <el-col :span="2">
           <el-select  v-model="queryBooks.select" placeholder="請选择">
              <el-option value="code" label="編碼" ></el-option>
              <el-option value="name" label="譯語" ></el-option>
            </el-select>
        </el-col>
        <el-col :span="10">
           <el-input placeholder="请输入查询内容" v-model="queryBooks.query">
            <el-button slot="append" icon="el-icon-search" @click="searchBooks"></el-button>
          </el-input>
        </el-col>
      </el-row>

      <!-- 用戶列表區 -->
      <el-table :data="booksList" stripe style="width: 100%" border>
        <el-table-column type="index" label="序號"></el-table-column>
        <el-table-column prop="code" label="編碼"></el-table-column>
        <el-table-column prop="name" label="譯語"></el-table-column>
      </el-table>
      <!-- 分頁區 -->
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="queryBooks.pagenum"
        :page-sizes="[5, 10,20,30]"
        :page-size="queryBooks.pagesize"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
      ></el-pagination>
    </el-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // 獲取書籍
      queryBooks: {
        query: "",
        pagenum: 1,
        pagesize: 10,
        select: ""
      },
      booksList: [],
      total: 0
    };
  },

  created() {
    this.getBooksList();
  },
  methods: {
    getBooksList() {

        this.$http.get(`/data/books`, {
          params: this.queryBooks
        })
        .then((res)=> {
          if (res.status !== 200) return this.message.error("獲取譯語表失敗!");
         
          this.booksList = res.data.data;
          this.total = res.data.total;

        })
        .catch((error)=> {
          console.log(error);
        });
      
    },

    searchBooks() {
      this.getBooksList();
     
    },
    //監聽pagesize改變的事件
    handleSizeChange(newSize) {
      this.queryBooks.pagesize = newSize;
      this.getBooksList();
    },
    // 監聽頁碼值改變的事件
    handleCurrentChange(newPage) {
      this.queryBooks.pagenum = newPage;
      this.getBooksList();
    }
  }
};
</script>


<style scoped>

</style>