# multi-lang-static-html-generator
multi-lang-static-html-generator

## install 

1. install poetry: `poetry install`
2. set env: `PYTHONPATH={now your project root}`
3. set google translation json key path: `GOOGLE_APPLICATION_CREDENTIALS={path of key}`


## usage

#### cli interface
* please execute in `{root of project}/app/interface/cmd`
* language code comply with iso 639-1
```
python generate.py --path {your_path} \
                   --src_lang {your_src_language_code} \
                   --dest_lang {your_dest_language_code}
```
* example command 
```
python generate.py --path /Users/dojunho/junho/multi-lang-static-sites/test/ko/tmp.html \
                   --src_lang ko \
                   --dest_lang en
```
