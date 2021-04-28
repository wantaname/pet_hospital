<template>
  <div class="container">
    <!--    卡片-->
    <el-card shadow="hover">
      <!--      头-->
      <div slot="header">
        <span class="title">{{header}}</span>
        <el-input placeholder="请输入内容" v-model="keyword" class="search">
          <el-select v-model="column" slot="prepend" placeholder="请选择">
            <el-option :label="item.label" :value="item.value" v-for="(item,index) in search.options" :key="index"></el-option>

          </el-select>
          <el-button slot="append" icon="el-icon-search" @click="clickSearch"></el-button>
        </el-input>
        <el-tag
            v-for="(tag,index) in tags"
            :key="index"
            closable
            @close="handleClose(tag)"
            type="success">
          {{tag.value}}
        </el-tag>
      </div>
      <!--      表格-->
      <el-table
          :data="tableData"
          stripe
          @selection-change="handleSelectionChange"
          style="width: 100%">
        <!--    多选-->
        <el-table-column
            type="selection"
            width="55"
            v-if="selectState">
        </el-table-column>
        <!--        列-->
        <el-table-column
            :prop="item.prop"
            :label="item.label"
            :width="item.width" v-for="(item,index) in table.table_columns" :key="index">
        </el-table-column>

        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button
                size="small"
                @click="handleEdit(scope.$index, scope.row)"
                icon="el-icon-edit-outline" circle type="primary" plain>
            </el-button>
          </template>
        </el-table-column>

      </el-table>

      <!--    分割线-->
      <el-divider></el-divider>
      <!--    操作区-->
      <div class="operate">
        <el-button @click="selectState=true" v-if="!selectState">多选</el-button>
        <el-button @click="selectState=false" type="danger" v-else>取消多选</el-button>

        <el-button @click="clickDelete" type="warning" v-if="selectState">删除</el-button>


        <el-button @click="clickAdd" type="primary" style="float: right">添加</el-button>

      </div>

    </el-card>

    <!--    添加对话框-->
    <el-dialog
        :title="addInfo.title"
        :visible.sync="addDialogVisible"
        :width="addInfo.width">
      <div>

        <el-form :model="addInfo.form" label-width="100px">
          <el-form-item :label="item.label" v-for="(item,index) in addInfo.form" style="width:80%">
            <el-input v-model="item.value" :type="item.type" :disabled="item.disabled" :rows="item.rows"></el-input>
          </el-form-item>

        </el-form>
      </div>

      <span slot="footer" class="dialog-footer">
    <el-button @click="addDialogVisible = false">取 消</el-button>
    <el-button type="primary" @click="addConfirm">确定</el-button>
  </span>
    </el-dialog>


    <!--编辑对话框-->
    <el-dialog
        :title="editInfo.title"
        :visible.sync="editDialogVisible"
        :width="editInfo.width">
      <div>

        <el-form :model="editInfo.form" label-width="100px">
          <el-form-item :label="item.label" v-for="(item,index) in editInfo.form" style="width:80%">
            <el-input v-model="item.value" :type="item.type" :disabled="item.disabled" :rows="item.rows"></el-input>
          </el-form-item>

        </el-form>
      </div>

      <span slot="footer" class="dialog-footer">
    <el-button @click="editDialogVisible = false">取 消</el-button>
    <el-button type="primary" @click="editConfirm">确定</el-button>
  </span>
    </el-dialog>

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
import config from "./config"
export default {
  data() {
    return {

      // 页面
      header:config.header,
      // 搜索
      search:config.search,
      //  表格
      table:config.table,
      //
      tableData: [],

      /*
      * 编辑
      * */
      // 编辑对话框
      editDialogVisible: false,
      //编辑数据
      editInfo: config.editInfo,

      //  多选状态
      selectState: false,
      //  多选的值，是一个id的数组
      multiSelectVal: [],

      /*
      搜索
      * */
      // 关键字
      keyword: config.search.keyword,
      // 搜素项
      column: config.search.column,
      //  搜索标签
      tags: [],

      //  分页
      page: config.page,


      /*
      * 添加数据
      * */
      // 显示对话框
      addDialogVisible: false,
      addInfo: config.addInfo,

      request: config.request
    }
  },
  created() {
    //  获取数据
    this.getData()
  },

  methods: {

    //移除标签
    handleClose(tag) {
      this.tags.splice(this.tags.indexOf(tag), 1);
    },

    //点击搜索
    clickSearch() {
      var t = {"name":this.column,"value":this.keyword}
      this.tags.push(t)
      // 初始化分页
      this.page.total = 0
      this.pagesize = 10
      this.pagenum = 1
      this.getData()
    },


    //点击编辑
    handleEdit(index, row) {
      //打开对话框
      this.editDialogVisible = true
      console.log(index, row);
      //根据id获得信息
      this.getEditDataById({column:"id",keyword:row.id})

    },
    getEditDataById(item){
      this.$http
          .get(this.request.getData.url, {
            params: {
              column:item.column,
              keyword:item.keyword,
              pagenum:1,
              pagesize:1,
            }
          })
          .then(res => {
            if (res.status !== 200) return this.message.error("获取信息失败!");
            console.log(res.data)
            let form = this.editInfo.form
            for(let item in form){
              form[item].value = res.data.data[0][item]
            }

          })
          .catch(error => {
            console.log(error);
          });
    },

    // 搜素
    getData() {

      this.$http
          .get(this.request.getData.url, {
            params: {
              column:this.column,
              keyword:this.keyword,
              pagenum:this.page.pagenum,
              pagesize:this.page.pagesize
            }
          })
          .then(res => {
            if (res.status !== 200) return this.message.error("获取信息失败!");
            this.tableData = res.data.data
            console.log(this.tableData)
            for(let item of this.tableData) {
              item.text = item.text.slice(0, 100)+"......"
            }

            this.page.total = res.data.total
          })
          .catch(error => {
            console.log(error);
          });
    },
//  根据id提交编辑
    editConfirm(){
      let request_items = this.request.edit.data
      let data = {}
      for(let i of request_items){
        data[i] = this.editInfo.form[i].value
      }
      this.$http
          .post(this.request.edit.url, data)
          .then(res => {

            if (res.data.status == 404) {
              this.$message.error("用户未登录");

            } else if (res.data.status == 300) {

              return this.$message.error(res.data.msg)
            } else if (res.data.status == 200) {
              this.$message.success("修改成功！")
              this.editDialogVisible = false
              this.getData()
            }
          })
          .catch(error => {

            console.log(error);
            return this.$message.error("系统错误！");

          });
    },

    // 处理选择的id
    handleSelectionChange(val) {
      var res = []
      for (var i = 0; i < val.length; i++) {
        res.push(val[i].id)
      }
      this.multiSelectVal = res
      console.log(this.multiSelectVal)
    },
    //添加功能
    clickAdd() {
      // this.$router.push({path: '/addPatient'})
      this.addDialogVisible = true
    },

    addConfirm() {
      let request_items = this.request.add.data
      let data = {}
      for(let i of request_items){
        data[i] = this.addInfo.form[i].value
      }
      this.$http
          .post(this.request.add.url, data)
          .then(res => {

            if (res.data.status == 404) {
              this.$message.error("用户未登录");

            } else if (res.data.status == 300) {

              return this.$message.error(res.data.msg)
            } else if (res.data.status == 200) {
              this.$message.success("添加成功！")
              this.addDialogVisible = false
              this.getData()

              //重置表单
              for(let i in this.addInfo.form){
                this.addInfo.form[i].value = ""
              }
            }
          })
          .catch(error => {

            console.log(error);
            return this.$message.error("系统错误！");

          });
    },

    //删除功能，根据id删除
    clickDelete() {
      this.$http
          .post(this.request.delete.url, {
            ids: this.multiSelectVal
          })
          .then(res => {

            if (res.data.status == 404) {
              this.$message.error("用户未登录");

            } else if (res.data.status == 300) {

              return this.$message.error(res.data.msg)
            } else if (res.data.status == 200) {
              this.$message.success("删除成功！")
              this.multiSelectVal = []
              this.selectState = false
              //  重新加载
              this.getData()
            }
          })
          .catch(error => {

            console.log(error);
            return this.$message.error("系统错误！");

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
.el-tag {
  margin-left: 10px;
}

.search {
  width: 40%;
  margin-left: 50px;
}

.title {
  color: #11ABF8;
}

.search {
  margin-right: 20px;
}
</style>