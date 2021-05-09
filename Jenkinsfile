pipeline{
 agent any
    stages{
       stage("build"){
             steps{
                echo 'build stage'
          }
    }
    stage("test"){
             steps{
             		echo 'Test stage'
                  }
        }

    stage("deploy"){
             steps{
              when {
              branch 'master'
              }
             	echo 'Deploy'
              sh 'python3 hello.py'
           }
    }

    }

}
