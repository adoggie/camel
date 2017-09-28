#!/bin/bash

basename=$(cd `dirname $0` ; pwd)

alias cp="cp -f"

python $TCE/bin/tmake/tce2py.py -i koala.idl,mgws.idl,mexs.idl -o ../


#cp ../koala/koala.py ../../src/sdk/python/libpushmessage_client/koala_imp.py
#mv ../koala/koala.py ../koala/koala_impl.py


#mkdir -p ../../src/sdk/java/lib/com/sw2us
#python $TCE/tce2java.py -i koala.idl,gws.idl,mexs.idl -o ../../src/sdk/java/lib/com/sw2us -p com.sw2us

python $TCE/bin/tmake/tce2js_requirejs.py -i koala.idl,mgws.idl,mexs.idl -o ./
python $TCE/bin/tmake/tce2js_requirejs.py -i koala.idl,mgws.idl,mexs.idl -o ../../sdk/html5/examples/scripts

rm -f parser.out parsetab.py



#python $TCE/tce2js.py -i lemon.idl,tgs.idl,mexs.idl -o ../libs
#rm -f parser.out parsetab.py
