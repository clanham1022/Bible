import os
os.system("clear") ;
os.system("cat bible_out/prefix   > bible_out/bible.tex") ;
# ----------------------------------
# the bible source includes
# 1: cuv1; 2: lzz; 3: kjv; 4: cuv2; 5: cnvv; 6: nrsv; 7: wenl
# ----------------------------------
fp_index    = open( "bibleIndex.txt"      , "r" )
str_index   = fp_index.readlines()
fp_index.close()
fp          = open( "bible_out/bible.tex" , "a" )
# cross referencing index to be added
# by 1 whenever there is a new section
xrefCnt     = 1
xbkCnt      = 0
for lines in str_index :
    xbkCnt += 1
    words   = lines.replace("\n","").split()
    # -------------------------------------------------------------------
    # words[0] words[1] words[2] words[3] Chi title abrev Eng title abrev
    # -------------------------------------------------------------------
    print( "----------------------------" )
    print( words[0] + " " + words[2]      )
    print( "----------------------------" )
    # -------------------
    # open the four bible
    # -------------------
    fp_cuv1 = open( "bible_src/cuv1/"    + words[3] + ".txt" ) ; content_cuv1 = fp_cuv1.readlines() ; fp_cuv1.close()
    fp_lzzv = open( "bible_src/lzz/"     + words[3] + ".txt" ) ; content_lzzv = fp_lzzv.readlines() ; fp_lzzv.close()
    fp_kjvv = open( "bible_src/kjv/"     + words[3] + ".txt" ) ; content_kjvv = fp_kjvv.readlines() ; fp_kjvv.close()
    fp_cuv2 = open( "bible_src/cuv2/"    + words[3] + ".txt" ) ; content_cuv2 = fp_cuv2.readlines() ; fp_cuv2.close()
    fp_cnvv = open( "bible_src/cnv/"     + words[3] + ".txt" ) ; content_cnvv = fp_cnvv.readlines() ; fp_cnvv.close()
    fp_nrsv = open( "bible_src/nrsv/"    + words[3] + ".txt" ) ; content_nrsv = fp_nrsv.readlines() ; fp_nrsv.close()
    fp_wenl = open( "bible_src/wenl/"    + words[3] + ".txt" ) ; content_wenl = fp_wenl.readlines() ; fp_wenl.close()
    # fp_msgv = open( "bible_src/msg/"     + words[3] ) ; content_msgv = fp_msgv.readlines() ; fp_msgv.close()
    # -----------------------------------------------------
    # [ GEN LATEX ] : create \chapter{} for current segment
    # -----------------------------------------------------
    print( words[0]+words[2] )
    fp.write( "\\chapter{"+words[0]+" "+words[2]+"}\n" )
    fp.write( "\\label{subsec:book"+str(xbkCnt)+"}\n"  )
    fp.write( "\\begin{multicols}{2}\n"                )
    fp.write( "\\minitoc\n"                            )
    fp.write( "\\end{multicols}\n"                     )
    # ------------------------------------------
    # check total chapter number in this segment
    # ------------------------------------------
    # -------
    # cuv1
    # -------
    sentenceNum = len( content_cuv1 )
    print("sentence no. in cuv1 "+words[3]+" is "+str(sentenceNum))
    chapterNum  = int( content_cuv1[ sentenceNum - 1 ].split(".")[0] )
    print("cuv1 "+words[3]+" contains "+str(chapterNum)+" chapters")
    # -------
    # lzzv
    # -------
    sentenceNum = len( content_lzzv )
    print("sentence no. in lzzv "+words[3]+" is "+str(sentenceNum))
    chapterNum  = int( content_lzzv[ sentenceNum - 1 ].split(".")[0] )
    print("lzzv "+words[3]+" contains "+str(chapterNum)+" chapters")
    # -------
    # kjvv
    # -------
    sentenceNum = len( content_kjvv )
    print("sentence no. in kjvv "+words[3]+" is "+str(sentenceNum))
    chapterNum  = int( content_kjvv[ sentenceNum - 1 ].split(".")[0] )
    print("kjvv "+words[3]+" contains "+str(chapterNum)+" chapters")
    # -------
    # cuv2
    # -------
    sentenceNum = len( content_cuv2 )
    print("sentence no. in cuv2 "+words[3]+" is "+str(sentenceNum))
    chapterNum  = int( content_cuv2[ sentenceNum - 1 ].split(".")[0] )
    print("cuv2 "+words[3]+" contains "+str(chapterNum)+" chapters")
    # -------
    # cnvv
    # -------
    sentenceNum = len( content_cnvv )
    print("sentence no. in cnvv "+words[3]+" is "+str(sentenceNum))
    chapterNum  = int( content_cnvv[ sentenceNum - 1 ].split(".")[0] )
    print("cnvv "+words[3]+" contains "+str(chapterNum)+" chapters")
    # -------
    # nrsv
    # -------
    sentenceNum = len( content_nrsv )
    print("sentence no. in nrsv "+words[3]+" is "+str(sentenceNum))
    chapterNum  = int( content_nrsv[ sentenceNum - 1 ].split(".")[0] )
    print("nrsv "+words[3]+" contains "+str(chapterNum)+" chapters")
    # -------
    # wenl
    # -------
    sentenceNum = len( content_wenl )
    print("sentence no. in wenl "+words[3]+" is "+str(sentenceNum))
    chapterNum  = int( content_wenl[ sentenceNum - 1 ].split(".")[0] )
    print("wenl "+words[3]+" contains "+str(chapterNum)+" chapters")
    # # -------
    # # msgv
    # # -------
    # sentenceNum = len( content_msgv )
    # print("sentence no. in msgv "+words[3]+" is "+str(sentenceNum))
    # chapterNum  = int( content_msgv[ sentenceNum - 1 ].split(".")[0] )
    # print("msgv "+words[3]+" contains "+str(chapterNum)+" chapters")
    # -----------------------------
    # check sentenceNum per chapter
    # -----------------------------
    sentenceNumPerChapter = {}
    #colorIntensity        = 15
    colorIntensity        = 100
    colorArr              =['CUV1LightRed'   , \
                            'LZZVLightGray'  , \
                            'KJVVLightGreen' , \
                            'CUV2LightYellow', \
                            'CNVVLightBrown' , \
                            'NRSVLightBlue'  , \
                            'WENLLightPurple']
    for chapterIdx in range(1,chapterNum+1,1) :
        # <<<< when a new version is added, no. of "c" in tabular requires adjustment >>>>
        bibleStr = "\section{"+words[0]+" "+words[2]+" "+str(chapterIdx)+"}" \
                   +" \hyperlink{toc}{[返主目錄]} \hyperref[subsec:book"+str(xbkCnt)+"]{[返卷目錄]}~\\begin{tabular}{ccccccc}\\cellcolor{" \
                   +colorArr[0]+"!"+str(colorIntensity)+"}CUV&\\cellcolor{"      \
                   +colorArr[1]+"!"+str(colorIntensity)+"}LZZ&\\cellcolor{"      \
                   +colorArr[2]+"!"+str(colorIntensity)+"}KJV&\\cellcolor{"      \
                   +colorArr[3]+"!"+str(colorIntensity)+"}CUVR&\\cellcolor{"     \
                   +colorArr[4]+"!"+str(colorIntensity)+"}CNV&\\cellcolor{"      \
                   +colorArr[5]+"!"+str(colorIntensity)+"}NRSV&\\cellcolor{"     \
                   +colorArr[6]+"!"+str(colorIntensity)+"}WLV"                   \
                   +"\\end{tabular}"                                             \
                   +"\\label{sec:"+str(xrefCnt)+"}"                              \
                   +"\n"
        fp.write( bibleStr )
        fp.write( "\\newline\n" )
        fp.write( "\\hyperref[sec:"+str(xrefCnt-1)+"]{< < < PREV CHAPTER < < <} ~~~ \\hyperref[sec:"+str(xrefCnt+1)+"]{> > > NEXT CHAPTER > > >} \\newline \n" )
        xrefCnt += 1
        for sentenceIdx in range(0,sentenceNum,1) :
            if ( chapterIdx < 10 and int(content_cuv1[sentenceIdx].split(".")[0]) == chapterIdx ) or \
               ( chapterIdx > 9  and int(content_cuv1[sentenceIdx].split(".")[0]) == chapterIdx ) :
                bibleStr = "\\begin{tabularx}{\\textwidth}{|c|X|}\n"  ; fp.write( bibleStr )
                bibleStr = "\hline\n"                                 ; fp.write( bibleStr )
                bibleStr = content_cuv1[sentenceIdx].replace("\n","")
                bibleStr = bibleStr.split(" ",1)
                # <<<< when a new version is added, argument in "multirow" requires adjustment >>>>
                bibleStr1= "\\multirow{7}{*}{\\rotatebox[origin=c]{90}{\\hfill "+words[1]+" "+words[3]+" $"+bibleStr[0]+"$ \\hfill}}" ; fp.write( bibleStr1)
                # ---------------------------------------------------
                # add the content of cuv1 to 1st row
                # ---------------------------------------------------
                bibleStr2= " & "+"\\cellcolor{"+colorArr[0]+"!"+str(colorIntensity)+"}"+bibleStr[1]+" \\\\\n" ; fp.write( bibleStr2)
                # ----------------------------------------------------
                # add the content of lzzv to 2nd row
                # ----------------------------------------------------
                bibleStr = content_lzzv[sentenceIdx].replace("\n","")
                bibleStr = bibleStr.split(" ",1)
                bibleStr = bibleStr[1]
                bibleStr = " & "+"\\cellcolor{"+colorArr[1]+"!"+str(colorIntensity)+"}"+bibleStr+" \\\\\n" ; fp.write( bibleStr )
                # ----------------------------------------------------
                # add the content of kjvv to 3rd row
                # ----------------------------------------------------
                bibleStr = content_kjvv[sentenceIdx].replace("\n","")
                bibleStr = bibleStr.split(" ",1)
                bibleStr = bibleStr[1]
                bibleStr = " & "+"\\cellcolor{"+colorArr[2]+"!"+str(colorIntensity)+"}"+bibleStr+" \\\\\n" ; fp.write( bibleStr ) ;
                # ----------------------------------------------------
                # add the content of cuv2 to 4th row
                # ----------------------------------------------------
                bibleStr = content_cuv2[sentenceIdx].replace("\n","")
                bibleStr = bibleStr.split(" ",1)
                bibleStr = bibleStr[1]
                bibleStr = " & "+"\\cellcolor{"+colorArr[3]+"!"+str(colorIntensity)+"}"+bibleStr+" \\\\\n" ; fp.write( bibleStr )
                # ----------------------------------------------------
                # add the content of cnvv to 5th row
                # ----------------------------------------------------
                bibleStr = content_cnvv[sentenceIdx].replace("\n","")
                bibleStr = bibleStr.split(" ",1)
                bibleStr = bibleStr[1]
                bibleStr = " & "+"\\cellcolor{"+colorArr[4]+"!"+str(colorIntensity)+"}"+bibleStr+" \\\\\n" ; fp.write( bibleStr )
                # ----------------------------------------------------
                # add the content of nrsv to 6th row
                # ----------------------------------------------------
                bibleStr = content_nrsv[sentenceIdx].replace("\n","")
                bibleStr = bibleStr.split(" ",1)
                bibleStr = bibleStr[1]
                bibleStr = " & "+"\\cellcolor{"+colorArr[5]+"!"+str(colorIntensity)+"}"+bibleStr+" \\\\\n" ; fp.write( bibleStr )
                # ---------------------------------------------------
                # add the content of wenl to 7th row
                # ---------------------------------------------------
                bibleStr = content_wenl[sentenceIdx].replace("\n","")
                bibleStr1 = []
                for c in bibleStr :
                    if ( not c.isdigit() ) and ( not c == "." ) :
                        bibleStr1.append(c)
                bibleStr = " & "+"\\cellcolor{"+colorArr[6]+"!"+str(colorIntensity)+"}"+''.join(bibleStr1)+" \\\\\n" ; fp.write( bibleStr )
                # # ----------------------------------------------------
                # # add the content of msgv to 7th row
                # # ----------------------------------------------------
                # bibleStr = content_msgv[sentenceIdx].replace("\n","")
                # bibleStr = bibleStr.split(" ",1)
                # bibleStr = bibleStr[1]
                # bibleStr = " & "+"\\cellcolor{"+colorArr[6]+"!"+str(colorIntensity)+"}"+bibleStr+" \\\\\n" ; fp.write( bibleStr )
                # ---------------------------------------------------
                # end current sentence
                # ---------------------------------------------------
                bibleStr = "\hline\n"                                 ; fp.write( bibleStr )
                bibleStr = "\end{tabularx}\n"                         ; fp.write( bibleStr )
fp.close()
os.system("cat bible_out/afterword >> bible_out/bible.tex")
os.system("cat bible_out/postfix >> bible_out/bible.tex")
