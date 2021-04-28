<template>
  <div class="container">
    <el-card shadow="hover">
      <div slot="header">
        <span class="title">定点医院</span>
        <el-input placeholder="请输入内容" v-model="keyword" class="search">
          <el-select v-model="column" slot="prepend" placeholder="请选择">
            <el-option label="全部" value="all"></el-option>
            <el-option label="地址" value="address"></el-option>
            <el-option label="医院" value="hospital"></el-option>
            <el-option label="类别" value="class"></el-option>

          </el-select>
          <el-button slot="append" icon="el-icon-search" @click="clickSearch"></el-button>
        </el-input>
        <el-button @click="clickMap" type="text" icon="el-icon-view" style="font-size: 28px;float:right"></el-button>

      </div>
      <iframe src="http://datanews.caixin.com/interactive/2020/fever/" v-if="showmap" class="frame"></iframe>
      <el-table
          :data="tableData"
          stripe
          @selection-change="handleSelectionChange"
          style="width: 100%"
      v-else>
        <!--    多选-->
        <el-table-column
            type="selection"
            width="55"
            v-if="selectState">
        </el-table-column>

        <el-table-column
            prop="id"
            label="id"
        >
        </el-table-column>
        <el-table-column
            prop="address"
            label="地址"
        >
        </el-table-column>
        <el-table-column
            prop="hospital"
            label="医院"
        >
        </el-table-column>
          <el-table-column
              prop="class"
              label="类别"
          >
        </el-table-column>


        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button
                size="small"
                @click="handleEdit(scope.$index, scope.row)"
                icon="el-icon-edit-outline" circle>
            </el-button>
          </template>
        </el-table-column>
      </el-table>

      <!--    分割线-->
      <el-divider></el-divider>
      <!--    操作区-->
      <div class="operate" v-if="!showmap">
        <el-button @click="selectState=true" v-if="!selectState">多选</el-button>
        <el-button @click="selectState=false" type="danger" v-else>取消多选</el-button>

        <el-button @click="clickDelete" type="warning" v-if="selectState">删除</el-button>


        <el-button @click="clickAdd" type="primary" style="float: right">添加</el-button>

      </div>

    </el-card>

    <!--编辑对话框-->
    <el-dialog
        title="编辑医院"
        :visible.sync="dialogVisible"
        width="45%">
      <div>
        <el-form ref="baseInfoForm" :model="baseInfo" label-width="120px">

          <el-form-item label="id" prop="id">
            <el-input v-model="baseInfo.id" disabled></el-input>
          </el-form-item>
          <el-form-item label="地址" prop="address">
            <el-input v-model="baseInfo.address"></el-input>
          </el-form-item>
          <el-form-item label="医院" prop="hospital">
            <el-input v-model="baseInfo.hospital"></el-input>
          </el-form-item>
          <el-form-item label="类别" prop="class">
            <el-input v-model="baseInfo.class"></el-input>
          </el-form-item>


        </el-form>
      </div>
      <span slot="footer" class="dialog-footer">
    <el-button @click="dialogVisible = false">取 消</el-button>
    <el-button type="primary" @click="confirm">确定</el-button>
  </span>
    </el-dialog>

    <!--    添加对话框-->

    <el-dialog
        title="添加医院"
        :visible.sync="addDialogVisible"
        width="45%">
      <div>
        <el-form ref="addInfoForm" :model="addInfo" label-width="120px">
          <el-form-item label="地址" prop="address">
            <el-input v-model="addInfo.address"></el-input>
          </el-form-item>
          <el-form-item label="医院" prop="hospital">
            <el-input v-model="addInfo.hospital"></el-input>
          </el-form-item>
          <el-form-item label="类别" prop="class">
            <el-input v-model="addInfo.class"></el-input>
          </el-form-item>
        </el-form>
      </div>
      <span slot="footer" class="dialog-footer">
    <el-button @click="addDialogVisible = false">取 消</el-button>
    <el-button type="primary" @click="addConfirm">确定</el-button>
  </span>
    </el-dialog>

    <!--    分页-->
    <!-- 分頁區 -->
    <el-pagination
        v-if="!showmap"
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

      dialogVisible:false,
      showmap:false,
      //添加对话框
      addDialogVisible:false,
      addInfo:{
        address:"",
        type:"",
        class:""
      },
      //编辑数据
      options:[],
      baseInfo:{

      },
      //  多选状态
      selectState: false,
      //  多选的值
      multiSelectVal: [],
      keyword: "",
      column: "all",
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
    clickMap(){
      this.showmap=!this.showmap
    },
    addConfirm(){
      this.$http
          .post("/hospital/addHospital", {
            addInfo:this.addInfo,

          })
          .then(res => {

            if (res.data.status == 404) {
              this.$message.error("用户未登录");

            }

            else if(res.data.status == 300)
            {

              return this.$message.error(res.data.msg)
            }
            else if (res.data.status == 200)
            {
              this.$message.success("添加成功！")
              this.addDialogVisible=false
              this.getData()
            }
          })
          .catch(error => {

            console.log(error);
            return this.$message.error("系统错误！");

          });
    },
    //点击搜索
    clickSearch(){
      this.getData()
    },
    //提交修改
    confirm(){
      this.editPatient()
    },
    //确认添加
    editPatient(){
      this.$http
          .post("/hospital/editHospital", {
            baseInfo:this.baseInfo,

          })
          .then(res => {

            if (res.data.status == 404) {
              this.$message.error("用户未登录");

            }

            else if(res.data.status == 300)
            {

              return this.$message.error(res.data.msg)
            }
            else if (res.data.status == 200)
            {
              this.$message.success("修改成功！")
              this.dialogVisible=false
              this.getData()
            }
          })
          .catch(error => {

            console.log(error);
            return this.$message.error("系统错误！");

          });
    },

    //点击编辑
    handleEdit(index, row) {
      //打开对话框
      this.dialogVisible=true
      //根据id获得信息
      this.getPatientById(row.id)

    },
    getPatientById(id){
      this.$http
          .get(`/hospital/getHospital`,{
            params:{
              id
            }
          })
          .then(res => {
            if (res.status !== 200) return this.message.error("获取信息失败!");

            this.baseInfo = res.data.data
          })
          .catch(error => {
            console.log(error);
          });
    },
//
    getPositionOptions(){
      this.$http
          .get(`/patient/getPositionOptions`)
          .then(res => {
            if (res.status !== 200) return this.message.error("获取省市信息失败!");

            this.options=res.data.data
          })
          .catch(error => {
            console.log(error);
          });
    },
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
      this.addDialogVisible=true
    },

    //删除功能
    clickDelete() {
      this.$http
          .post("/hospital/deleteHospital", {
            patientList: this.multiSelectVal
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
    getData() {
      this.$http
          .get(`/hospital/getHospital`,{
            params:{
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
.search{
  width: 40%;
  margin-left: 50px;
}
.frame{
  width: 100%;
  border: 0;
  height: 500px;
}
.title{
  color: #11ABF8;
}
</style>