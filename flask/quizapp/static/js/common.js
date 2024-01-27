// 回答ボタン処理
document.querySelector('#btnAnswer').addEventListener("click", () => {
    // 解説表示
    document.querySelectorAll('[data-question-correct]').forEach((e,idx) => { 
        document.querySelector(`#explanation_no_${idx + 1}`).style.visibility = 'visible';
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
            .filter(e2 => e2.checked && e.dataset.questionCorrect === e2.value )
            .forEach(e2 => e2.parentElement.classList.add('bg-Success'));
    });

    // 不正解のスタイル制御
    document.querySelectorAll('[data-question-correct]').forEach((e,idx) => { 
        [...document.querySelectorAll(`[name="${e.id}"]`)]
            .filter(e2 => e2.checked && e.dataset.questionCorrect !== e2.value )
            .forEach(e2 => e2.parentElement.classList.add('bg-danger')) ;
    });

});