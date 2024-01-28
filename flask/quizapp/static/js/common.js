// 回答ボタン処理
document.querySelector('#btnAnswer').addEventListener("click", () => {

    // 全件数
    var totalCount = document.querySelectorAll('[data-question-correct]').length;
    // 正解数
    var correctCount = 0;
    document.querySelectorAll('[data-question-correct]').forEach((e,idx) => { 
        correctCount += [...document.querySelectorAll(`[name="${e.id}"]`)]
            .filter(e2 => e2.checked && e.dataset.questionCorrect === e2.value)
            .length
    });

    var comment = '';
    if (totalCount == 5) {
        if (correctCount == 0) {
            comment = ""
            + "少し落胆するかもしれませんが、大丈夫です。</br>"
            + "失敗は成長の機会です。今回の結果を振り返り、間違えた部分を理解し、次回に向けて学びを深めましょう。</br>"
            + "誰もが最初から完璧な成績を収めることは難しいことです。</br>"
            + "頭を下げずに、自分の能力を信じて、努力と継続を大切にしましょう。</br>"
            + "次回のチャレンジでより良い結果を得るために取り組んでください。成功への道は、失敗から始まることもあります。</br>"
        }
        if (correctCount == 1) {
            comment = ""
            + "まずはその1問の正解におめでとうございます！</br>"
            + "正解が1つあることは、あなたの知識や努力が実を結んだことを示しています。</br>"
            + "次回のチャレンジに向けて、この成功をモチベーションにしましょう。</br>"
            + "誤答からも学びを得て、知識やスキルを向上させる努力を続けてください。</br>"
            + "成功への道は、一歩ずつ進んでいくものです。応援しています！</br>"        
        }
        if (correctCount == 2) {
            comment = ""
            + "正解が2つあることは、あなたの知識や努力が実を結んだ証です。</br>"
            + "さらなる成長に向けて、この成功を励みにしてください。]</br>"
            + "間違えた問題についても学び、次回のチャレンジでさらに良い結果を出すために準備を続けましょう。</br>"
            + "成功は一歩ずつ積み重ねていくものです。頑張ってください！</br>"        
        }
        if (correctCount == 3) {
            comment = ""
            + "素晴らしい成績です！正解が3問もあることは、あなたの知識やスキルが高いことを示しています。</br>"
            + "この成功を自信に変え、更なる成長に向けて努力を続けてください。</br>"
            + "誤答についても学びを得て、次回のチャレンジでさらに良い結果を目指しましょう。</br>"
            + "成功への道は着実に進んでいることでしょう。おめでとうございます！</br>"
        }
        if (correctCount == 4) {
            comment = ""
            + "素晴らしい成績です！正解が4問もあることは、あなたの知識やスキルが高いことを示しています。</br>"
            + "この成功を自信に変え、更なる成長に向けて努力を続けてください。</br>"
            + "誤答についても学びを得て、次回のチャレンジでさらに良い結果を目指しましょう。</br>"
            + "成功への道は着実に進んでいることでしょう。おめでとうございます！</br>"        
        }
        if (correctCount == 5) {
            comment = ""
            + "おめでとうございます！これは完璧な成績です。</br>"
            + "全問正解ということは、あなたの高い知識とスキルを証明しています。</br>"
            + "この成功を誇りに思い、更なる目標に向かって前進しましょう。</br>"
            + "あなたの能力を信じ、学びを深め、新しいチャレンジに取り組んでください。</br>"
            + "あなたの未来には素晴らしい成果が待っていることでしょう。</br>"
            + "本当におめでとうございます！</br>"
        }
    }
    document.querySelector('.modal-body').innerHTML = '全' + totalCount + '問中、' + correctCount + '問あってました！</br></br>' + comment    ;

});

// モーダルcloseボタン処理
document.querySelector('#btnClose').addEventListener("click", () => {

    // 解説表示
    document.querySelectorAll('[data-question-correct]').forEach((e,idx) => { 
        document.querySelector(`#explanation_no_${idx + 1}`).style.display = 'block';
    });

    // 現在のチェック項目のスタイルを消す
    document.querySelectorAll('[data-question-correct]').forEach((e,idx) => { 
        [...document.querySelectorAll(`[name="${e.id}"]`)]
            .forEach(e2 => {
                e2.parentElement.classList.remove('bg-Success');
                e2.parentElement.classList.remove('bg-Secondary');
                e2.parentElement.classList.remove('bg-danger');
            });
    });

    // 正解／不正解に関係ない項目をグレーにする
    document.querySelectorAll('[data-question-correct]').forEach((e,idx) => { 
        [...document.querySelectorAll(`[name="${e.id}"]`)]
            .filter(e2 => !e2.checked)
            .forEach(e2 => e2.parentElement.classList.add('bg-Secondary'));
    });

    // 正解のスタイル制御
    document.querySelectorAll('[data-question-correct]').forEach((e,idx) => { 
        [...document.querySelectorAll(`[name="${e.id}"]`)]
            .filter(e2 => e.dataset.questionCorrect === e2.value )
            .forEach(e2 => e2.parentElement.classList.add('bg-Success'));
    });

    // 不正解のスタイル制御
    document.querySelectorAll('[data-question-correct]').forEach((e,idx) => { 
        [...document.querySelectorAll(`[name="${e.id}"]`)]
            .filter(e2 => e2.checked && e.dataset.questionCorrect !== e2.value )
            .forEach(e2 => e2.parentElement.classList.add('bg-danger')) ;
    });

});