import math
from frequencies import * 
from MLfunctions import *

cipher = "huvw !kzcq7nv3 qv3!hqv ,evwrhqv3rvq9qwi3qvhuv2cq,3vmk,7v,7zvbikb!kvhuvzqe3!7ufv3 qvmk,7nv,evuriv57r1nv!ev3rvieqv3 qvwreh!wvq73!3!qev57r17v,ev3 qv!7b!7!3uve3r7qev3rv1!mqv ,kbvrbv3 qvi7!;qceqvri3vrbvq9!e3q7wqverv3 ,3v3 qvr3 qcv ,kbvh,uv3 c!;qfvricv2cq,3qe3vw ,kkq72qv ,evtqq7vb!7z!72v3 qve3r7qev!7v3 !ev;,e3vi7!;qceqnvti3v7r1v3 quv,cqv1!3 !7vricv2c,emfv3 qvem,wqve3r7qnv57r1ev,kerv,ev3 qv3qeeqc,w3nvcqe!zqevr7v,e2,czfv,b3qcvkr5!evb,!kicqvr7vq,c3 nv3 rcv ,ev3,5q7v!3v,7zvmi3v!3v!7vrz!7ev;,ik3fv3 qvmr1qcve3r7qv!evr7vhrc,2fv!v ,;qvrczqcqzvcr7,7v3 qv,wwieqcv3rvcq3c!q;qv!3vbrcvhqnv!7vcq3ic7v!ve ,kkvzqe3cruv9,7z,cfv3 qvh!7zve3r7qv!evr7vq,c3 nv!vmi3v!3v!7v3 qve3,bbv!v2,;qv3rvkr5!nvti3v7r1v!v ,;qv q,czv3 ,3v!3v!evmr1qc!72v,vwutrc2v57r17v,ev3 qv;!e!r7fv3 qvcq,k!3uve3r7qv!evr7v3 qvwqkqe3!,kv q,zv57r17v,ev57r1 qcqfv!3v!ev1!3 v3,7qkqqcv3!;,7v!7v !evm,3 q3!wvwrkkqw3!r7nv2!b3qzv3rv !hvtuv3 qv,e2,cz!,7ev,b3qcv3 qvz,c5vqk;qevb,!kicqv!7v,wxi!c!72vbrcv3 qheqk;qefv3 qv3!hqve3r7qv!ev,kervr7vq,c3 nv1!3 v,v2crimvrbvercwqcqcenvwiccq73kuv2i,czqzvtuv3 q!cvkq,zqcnv3 qv,7w!q73vr7qfv3 qvk,e3ve3r7qnv3 qverikve3r7qnv ,evuq3v3rvtqvbri7znvti3v!v ,;qvmi3vhuvb,;ric!3qvz,i2 3qcnv2,hrc,nvr7v3rv!3ev3c,!knv,7zve qv ,ev7r3vz!e,mmr!73qzvhqvuq3fvr7wqv,ve3r7qv!evwrkkqw3qzv!v1!kkvtqv,tkqv3rv ,c7qeev!3evmr1qcvie!72v,v2,i73kq3v!v ,;qvrczqcqzv3 qvz1,c;qevr7v7!z,;qkk!cfv3 qv3!hqvbrcvwreh!wvrczqcv!ev7q,cnv,7zv1 q7v!vwrkkqw3v,kkv3 qve3r7qev!v1!kkv rkzvi7!;qceqv!7vhuv ,7zefv i2ev,7zv5!eeqenvv3 ,7re"

letters = "abcdefghijklmnopqrstuvwxyz1234567890!., -_'\":;/"
AmountOfLetters = len(letters)

Value = -100000
PreviousValue = -100000
count = 0

iterations = 20000

UnlockCode = generate(letters)

print(evaluate(cipher, frequencies))

for k in range(iterations):
    ProposedCode = dict(UnlockCode)
    
    ProposedCode = shuffle(ProposedCode)

    ProposedCipher = decipher(cipher, ProposedCode)
    UnlockCipher = decipher(cipher, UnlockCode)

    if evaluate(ProposedCipher, frequencies) > evaluate(UnlockCipher, frequencies):
        UnlockCode = dict(ProposedCode)

    Value = evaluate(UnlockCipher, frequencies)
    if Value > PreviousValue:
        print(Value, " / ", k)
        count = 0
        PreviousValue = Value
        continue
    else:
        count += 1

    PreviousValue = Value

    if count % 1000 == 0:
        print(evaluate(UnlockCipher, frequencies), " / ", k)

print(UnlockCode)
print(decipher(cipher, UnlockCode))