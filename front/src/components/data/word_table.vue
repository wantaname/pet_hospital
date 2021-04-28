<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/' }">首頁</el-breadcrumb-item>
      <el-breadcrumb-item>項目數據</el-breadcrumb-item>
      <el-breadcrumb-item>詞目表</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 卡片 -->
    <el-card class="box-card">
      <el-row :gutter="2">
        <el-col :span="2">
           <el-select  v-model="queryClass.select" placeholder="请选择">
              <el-option value="code" label="編碼" ></el-option>
              <el-option value="word" label="詞目" ></el-option>
              <el-option value="pron" label="對音" ></el-option>
              <el-option value="class" label="義類" ></el-option>
              <el-option value="type" label="譯語" ></el-option>
              <el-option value="note" label="備註" ></el-option>
            </el-select>
        </el-col>
        <el-col :span="10">
           <el-input placeholder="请输入查询内容" v-model="queryClass.query">
            <el-button slot="append" icon="el-icon-search" @click="searchClass"></el-button>
          </el-input>
        </el-col>
      </el-row>

      <!-- 用戶列表區 -->
      <el-table :data="classList" stripe style="width: 100%" border>
        <el-table-column type="index" label="序號"></el-table-column>
        <el-table-column prop="code" label="編碼"></el-table-column>
        <el-table-column prop="word" label="詞目"></el-table-column>
        <el-table-column prop="pron" label="對音"></el-table-column>
        <el-table-column prop="class" label="義類"></el-table-column>
        <el-table-column prop="type" label="譯語"></el-table-column>
        <el-table-column prop="note" label="備註"></el-table-column>
      </el-table>
      <!-- 分頁區 -->
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="queryClass.pagenum"
        :page-sizes="[5, 10,20,30]"
        :page-size="queryClass.pagesize"
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
      queryClass: {
        query: "",
        pagenum: 1,
        pagesize: 10,
        select: ""
      },
      classList: [],
      total: 0
    };
  },

  created() {
    this.getClassList();
  },
  methods: {
    getClassList() {

        this.$http.get(`/data/words`, {
          params: this.queryClass
        })
        .then((res)=> {
          if (res.status !== 200) return this.message.error("獲取詞目失敗!");
   
  
          this.classList = res.data.data;
          this.total = res.data.total;
        })
        .catch((error)=> {
          console.log(error);
        });
      
    },

    searchClass() {
      this.getClassList();
     
    },
    //監聽pagesize改變的事件
    handleSizeChange(newSize) {
      this.queryClass.pagesize = newSize;
      this.getClassList();
    },
    // 監聽頁碼值改變的事件
    handleCurrentChange(newPage) {
      this.queryClass.pagenum = newPage;
      this.getClassList();
    }
  }
};
</script>


<style scoped>

</style>