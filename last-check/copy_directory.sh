# ディレクトリごとコピーして、遷移先のファイルを開くスクリプト
# sh copy_directory.sh target_directory output_directory
# ex) sh copy_directory.sh 038 039

if [ $# -ne 1 ]; then
  echo "引数で対象ディレクトリを指定してください"
  exit 0
fi

cp -r templates $1 && cd $1 && code answer.py input.txt
