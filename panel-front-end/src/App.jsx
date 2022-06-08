import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import { Routes, Route, Link } from "solid-app-router";
import { onMount, createSignal, onCleanup } from "solid-js";

const api_url = "http://localhost:5000"

const [getAchievementsJson, setAchievementsJson] = createSignal("");

function ReturnMenu() {
    return (
        <Link href='/'>
            <button type="button" class="fs-1 text-white btn position-absolute top-0 start-0" style="background-color:#c45a8f; margin: 5px">
                Назад
            </button>
        </Link>
    )
}

function requestAchievements() {
    console.log("making request");
    const filters = document.getElementsByClassName("filter-list");
    const filter_data = {};
    for(let i = 0; i < filters.length; i++) {
        filter_data[filters[i].children[0].id] = "";
        const selections = filters[i].getElementsByClassName("selection-value");
        const selected = [];
        for(let j = 0; j < selections.length; j++) {
            if(selections[j].checked == true) {
                selected.push(selections[j].id);
            }
        }
        for(let j = 0; j < selected.length; j++) {
            if(j != selected.length - 1) {
                filter_data[filters[i].children[0].id] += selected[j] + ","
            } else {
                filter_data[filters[i].children[0].id] += selected[j]
            }
        }
    }

    let path = "/getachievements"
    let params = ""
    Object.entries(filter_data).map(item => {
        params += item[0] + "=" + item[1] + "&"
    })
    let dataReq = new XMLHttpRequest();
    dataReq.open("GET", api_url + path + "?" + params);
    dataReq.send();

    setAchievementsJson(JSON.stringify(filter_data));
}

function Filter(props) {
    // category = ["api_key", "human-readable string"]
    // selections = [["api_key", "string"]]
    const category = props.category;
    const selections = props.selections;
    let listener;
    onMount(() => {
        let checkList = document.getElementById(category[0] + '-list');
        checkList.getElementsByClassName('anchor')[0].onclick = function(evt) {
            if (checkList.classList.contains('visible')){
                checkList.classList.remove('visible');
            } else {
                checkList.classList.add('visible');
            }
        }

        listener = function(evt) {
            if (!document.getElementById(category[0] + "-list").contains(evt.target)) {
                if (checkList.classList.contains('visible'))
                checkList.classList.remove('visible');
            }
        };

        document.addEventListener("click", listener);

        console.log("filter mounted");
    })

    onCleanup(() => {
        document.removeEventListener("click", listener);
    })
    
    return (
        <div id={category[0] + "-list"} class="filter-list dropdown-check-list align-top" style="margin: 5px">
            <button id={category[0]} type="button" class="anchor fs-1 text-white btn" style="background-color:#c45a8f">
                <span>{category[1]}</span>
            </button>
            <ul class="items">
                <For each={selections}>{(selection, _i) =>
                    <li>
                        <button type="button" class="selection-button fs-3 text-white btn w-100 d-flex justify-content-left" style="padding: 0px">
                            <input id={selection[0]} type="checkbox" class="selection-value" onclick={() => requestAchievements()}/>
                            <label for={selection[0]} class="w-100 h-100 d-flex justify-content-left">
                                {selection[1]}
                            </label>
                        </button>
                    </li>
                }</For>
            </ul>
        </div>
    )
}

function MainMenu() {
    onMount(() => {
        console.log("main menu mounted");
    })
    return (
        <div class="h-100" style="font-family: 'efourpro'">
            <div class="container text-white h-100">
                <div class="row h-50">
                    <div class="col-sm d-flex justify-content-center align-items-center">
                        <Link href="/plan" class="w-75 h-50">
                            <button type="button" class="fs-1 text-white btn w-100 h-100" style="background-color:#c45a8f">структура школы</button>
                        </Link>
                    </div>
                    <div class="col-sm d-flex justify-content-center align-items-center">
                        <Link href="/achievements" class="w-75 h-50">
                            <button type="button" class="fs-1 text-white btn w-100 h-100" style="background-color:#c45a8f">достижения</button>
                        </Link>
                    </div>
                </div>
                <div class="row h-50">
                    <div class="col-sm d-flex justify-content-center align-items-center">
                        <Link href="/sections" class="w-75 h-50">
                            <button type="button" class="fs-1 text-white btn w-100 h-100" style="background-color:#c45a8f">кружки</button>
                        </Link>
                    </div>
                    <div class="col-sm d-flex justify-content-center align-items-center">
                        <Link href="/facts" class="w-75 h-50">
                            <button type="button" class="fs-1 text-white btn w-100 h-100" style="background-color:#c45a8f">факты</button>
                        </Link>
                    </div>
                </div>
            </div>
        </div>
    )
}

function Achievements() {
    onMount(() => {
        console.log("achievements mounted");
    })
    return (
        <div class="h-100" style="font-family: 'efourpro'">
            <ReturnMenu/>
            <div id="filters" class="position-absolute top-0 end-0">
                <Filter
                    category={["category", "категория"]}
                    selections={[
                        ["olympiad", "олимпиада"],
                        ["conference", "конференция"],
                        ["sport", "спорт"]
                    ]}
                />
                <Filter
                    category={["field", "область"]}
                    selections={[
                        ["informatics", "информатика"],
                        ["math", "математика"],
                        ["economy", "экономика"]
                    ]}
                />
            </div>
            <div class="d-flex justify-content-center align-items-center h-100">
                <code>
                    {getAchievementsJson()}
                </code>
            </div>
        </div>
    )
}

function Plan() {
    return (
        <div class="h-100" style="font-family: 'efourpro'">
            <ReturnMenu/>
            <h1 class="text-white h-100 d-flex justify-content-center align-items-center" style="font-family: 'efourpro'">
                Plan WIP
            </h1>
        </div>
    )
}

function Sections() {
    return (
        <div class="h-100" style="font-family: 'efourpro'">
            <ReturnMenu/>
            <h1 class="text-white h-100 d-flex justify-content-center align-items-center" style="font-family: 'efourpro'">
                Section WIP
            </h1>
        </div>
    )
}

function Facts() {
    return (
        <div class="h-100" style="font-family: 'efourpro'">
            <ReturnMenu/>
            <h1 class="text-white h-100 d-flex justify-content-center align-items-center" style="font-family: 'efourpro'">
                Facts WIP
            </h1>
        </div>
    )
}

function App() {
    return (
        <Routes>
            <Route path="/" element={<MainMenu/>} />
            <Route path="/achievements" element={<Achievements/>} />
            <Route path="/plan" element={<Plan/>} />
            <Route path="/sections" element={<Sections/> } />
            <Route path="/facts" element={<Facts/> } />
        </Routes>
    );
}


export default App;
