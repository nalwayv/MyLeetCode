package main

import "fmt"

// a simple queue dataset using a slice
type Queue []int

func (q *Queue) Length() int {
	return len(*q)
}

func (q *Queue) Enqueue(value int) {
	*q = append(*q, value)
}

func (q *Queue) Dequeue() int {
	value := (*q)[0]
	*q = (*q)[1:]
	return value
}

func (q *Queue) Peek() int {
	return (*q)[0]
}

// a simple set datastructure using a map to an empty stuct
type Set map[int]struct{}

func (s Set) Add(riderId int) {
	s[riderId] = struct{}{}
}

func (s Set) Remove(riderId int) {
	delete(s, riderId)
}

func (s Set) Has(riderId int) bool {
	_, ok := s[riderId]
	return ok
}

//
type RideSharingSystem struct {
	drivers   Queue
	riders    Queue
	cancelled Set
	booked    Set
}

func Constructor() RideSharingSystem {
	result := RideSharingSystem{}

	result.riders = Queue{}
	result.drivers = Queue{}
	result.booked = Set{}
	result.cancelled = Set{}

	return result
}

func (this *RideSharingSystem) AddRider(riderId int) {
	this.riders.Enqueue(riderId)
	this.booked.Add(riderId)
}

func (this *RideSharingSystem) AddDriver(driverId int) {
	this.drivers.Enqueue(driverId)

}

// Return a array comprised of both driver and riders id's if available else -1 for both
func (this *RideSharingSystem) MatchDriverWithRider() []int {
	// if no drivers then return
	if this.drivers.Length() == 0 {
		return []int{-1, -1}
	}

	// if current rider has canceled then move to the next
	for this.riders.Length() > 0 && this.cancelled.Has(this.riders.Peek()) {
		this.cancelled.Remove(this.riders.Dequeue())
	}

	// there moght be no riders after removing cancelled
	if this.riders.Length() == 0 {
		return []int{-1, -1}
	}

	// dispatch and update booked
	driver := this.drivers.Dequeue()
	rider := this.riders.Dequeue()

	this.booked.Remove(rider)

	return []int{driver, rider}
}

func (this *RideSharingSystem) CancelRider(riderId int) {
	if !this.booked.Has(riderId) {
		return
	}

	this.booked.Remove(riderId)
	this.cancelled.Add(riderId)
}

func main() {
	fmt.Println("3829. Design Ride Sharing System")

	var r RideSharingSystem = Constructor()

	r.AddRider(3)
	r.AddDriver(2)
	r.AddRider(1)

	var match1 []int = r.MatchDriverWithRider()
	fmt.Printf("Driver: %d, Rider: %d\n", match1[0], match1[1])

	r.AddDriver(5)

	var match2 []int = r.MatchDriverWithRider()
	fmt.Printf("Driver: %d, Rider: %d\n", match2[0], match2[1])

	var match3 []int = r.MatchDriverWithRider()
	fmt.Printf("Driver: %d, Rider: %d\n", match3[0], match3[1])
}
