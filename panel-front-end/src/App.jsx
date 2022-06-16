import '../node_modules/bootstrap/dist/css/bootstrap.min.css';

import plan1 from "./assets/1.jpg";
import plan2 from "./assets/2.jpg";
import plan4 from "./assets/4.jpg";
import plan5 from "./assets/5.jpg";

import { Routes, Route, Link } from "solid-app-router";
import { onMount, createSignal, onCleanup, Show, For } from "solid-js";

const api_url = "http://localhost:8000"

const [getAchievements, setAchievements] = createSignal([]);
const [getClubs, setClubs] = createSignal([]);
const [getFilters, setFilters] = createSignal([]);

function ReturnMenu() {
    return (
        <Link href='/'>
            <button type="button" class="fs-1 text-white btn position-absolute top-0 start-0" style="background-color:#c45a8f; margin: 5px">
                Назад
            </button>
        </Link>
    )
}

function requestData(setter, path) {
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

    let route = "/get" + path;
    let params = "";
    Object.entries(filter_data).map(item => {
        params += item[0] + "=" + item[1] + "&"
    })
    let dataReq = new XMLHttpRequest();
    dataReq.onreadystatechange = function() {
        if (dataReq.readyState === 4) {
            setter(JSON.parse(dataReq.response)[0]);
            setFilters(JSON.parse(dataReq.response)[1]);
        }
    }
    console.log(api_url + route + "/?" + params);
    dataReq.open("GET", api_url + route + "/?" + params, true);
    dataReq.send();
}

function Filter(props) {
    const category = props.category;
    const selections = props.selections;
    let listener;
    onMount(() => {
        let checkList = document.getElementById(category + '-list');
        checkList.getElementsByClassName('anchor')[0].onclick = function(evt) {
            if (checkList.classList.contains('visible')){
                checkList.classList.remove('visible');
            } else {
                checkList.classList.add('visible');
            }
        }

        listener = function(evt) {
            if (!document.getElementById(category + "-list").contains(evt.target)) {
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
        <div id={category + "-list"} class="filter-list dropdown-check-list align-top" style="margin: 5px">
            <button id={category} type="button" class="anchor fs-1 text-white btn" style="background-color:#c45a8f">
                <span>{category}</span>
            </button>
            <ul class="items">
                <For each={selections}>{(selection, _i) =>
                    <li>
                        <button type="button" class="selection-button fs-3 text-white btn w-100 d-flex justify-content-left" style="padding: 0px">
                            <input id={selection} type="checkbox" class="selection-value" onclick={() => requestData(props.setter, props.path)}/>
                            <label for={selection} class="w-100 h-100 d-flex justify-content-left">
                                {selection}
                            </label>
                        </button>
                    </li>
                }</For>
            </ul>
        </div>
    )
}

function AllFilters(props) {
    return (
        <div id="filters" class="position-absolute top-0 end-0">
            <For each={Object.keys(getFilters())}>{(filter, _i) => 
                <Filter
                    category={filter}
                    selections={getFilters()[filter]}
                    setter={props.setter}
                    path={props.path}
                />
            }</For>
        </div>
    )
}

function AchievementCard(props) {
    return(
        <div style="background-color:#c45a8f; margin:10px; height:25vh; width:25vw; padding: 10px" class="rounded">
            <div class="d-flex justify-content-start">
                <div style="height: 100px; width: 100px; background: #888888">
                </div>
                <div style="margin:10px">
                    Событие: {props.achievement[1]}<br/>
                    Предмет: {props.achievement[5]}<br/>
                </div>
            </div>
            <div>
                Участники: {props.achievement[6]}<br/>
                Награда: {props.achievement[7]}<br/>
            </div>
        </div>
    )
}

function ClubCard(props) {
    return(
        <div style="background-color:#c45a8f; margin:10px; height:25vh; width:25vw; padding: 10px" class="rounded">
            <div class="d-flex justify-content-start">
                <div style="height: 100px; width: 100px; background: #888888">
                </div>
                <div style="margin:10px">
                    Кружок: {props.club[0]}<br/>
                    Ведущий: {props.club[1]}<br/>
                    Категория: {props.club[2]}<br/>
                </div>
            </div>
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
                        <Link href="/clubs" class="w-75 h-50">
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
        requestData(setAchievements, "achievements")
        console.log("achievements mounted");
    })
    return (
        <div class="h-100 container" style="font-family: 'efourpro'">
            <div class="row">
                <header>
                    <ReturnMenu/>
                    <AllFilters setter={setAchievements} path="achievements"/>
                </header>
            </div>
            <div class="row" style="font-family: 'Roboto', sans-serif;">
                <div class="container w-75">
                    <div class="row row-cols-2">
                        <For each={getAchievements()}>{(achievement, _i) =>
                        <>
                            <div class="col h-25">
                                <AchievementCard achievement={achievement}/>
                            </div>
                            <Show when={_i() % 2 == 1}>
                                <div class="w-100"></div>
                            </Show>
                        </>
                        }</For>
                    </div>
                </div>
            </div>
        </div>
    )
}

function Clubs() {
    onMount(() => {
        requestData(setClubs, "hobbies")
        console.log("clubs mounted");
    })
    return (
        <div class="h-100" style="font-family: 'efourpro'">
            <div class="row">
                <header>
                    <ReturnMenu/>
                    <AllFilters setter={setClubs} path="hobbies"/>
                </header>
            </div>
            <div class="row" style="font-family: 'Roboto', sans-serif; margin:0px">
                <div class="container w-75">
                    <div class="row row-cols-2">
                        <For each={getClubs()}>{(club, _i) =>
                        <>
                            <div class="col h-25">
                                <ClubCard club={club}/>
                            </div>
                            <Show when={_i() % 2 == 1}>
                                <div class="w-100"></div>
                            </Show>
                        </>
                        }</For>
                    </div>
                </div>
            </div>
        </div>
    )
}

function Plan() {
    return (
        <div class="h-100" style="font-family: 'efourpro'">
            <ReturnMenu/>
            <img src={plan1} class="w-100" />
            <img src={plan2} class="w-100" />
            <img src={plan4} class="w-100" />
            <img src={plan5} class="w-100" />
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
            <Route path="/clubs" element={<Clubs/> } />
            <Route path="/facts" element={<Facts/> } />
        </Routes>
    );
}


export default App;
