# ディレクトリごとコピーして、遷移先のファイルを開くスクリプト
# sh copy_directory.sh target_directory output_directory
# ex) sh copy_directory.sh 038 039

if [ $# -ne 2 ]; then
  echo "２つの引数で実行してください"
  exit 0
fi

cp -r $1 $2 && cd $2 && code answer.py input.txt
